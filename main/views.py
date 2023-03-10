# Django imports
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Model imports
from .models import Player
from .models import Team

# Form imports
from .forms import PlayerForm
from .forms import UpgradeForm

# Custom imports
from .discord import auth as discord_auth
from .league import config as league_config

# Custom packages
from .league.player import upgrade as hoops_player_upgrade
from .league.player import create as hoops_player_create
from .league.extra import convert as hoops_extra_convert

# .ENV file import
import os, json
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def home(request):
    current_user = request.user
    context = {
        "title": "Home",
        "current_user": current_user,
        "players": [],
    }
    # Send players to home page
    if current_user.is_authenticated:
        players = Player.objects.filter(discord_user=current_user)
        for p in players:
            context["players"].append(p)
    # Return the home page
    return render(request, "main/league/home.html", context)

def login(request):
    return HttpResponse("This is the login page.")

def login_discord(request):
    discord_auth_url = os.environ.get("DISCORD_AUTH_URL")
    return redirect(discord_auth_url)

def login_discord_redirect(request):
    try:
        # Get information from Discord
        code = request.GET.get('code')
        info = discord_auth.exchange_code(code)
        user = info[0]
        guilds = info[1]
        # Create the discord user
        discord_user = authenticate(request, user=user)
        discord_user = list(discord_user).pop()
        # Finally, log the user in
        django_login(request, discord_user, backend="main.authorize.DiscordBackend")
    except:
        pass
    return redirect(home)

def logout(request):
    django_logout(request)
    return redirect("/")

def player(request, id):
    # Check if the player exists
    try:
        plr = Player.objects.get(pk=id)
    except Player.DoesNotExist:
        return HttpResponse("Sorry, this player doesn't exist!")
    # Initialize the context
    context = {
        "title": f"{plr.first_name} {plr.last_name}",
        "player": plr,
    }
    return render(request, "main/players/player.html", context)

@login_required(login_url="/login/discord/")
def upgrade_player(request, id):
    # Collect user & player information
    user = request.user
    # Check if the player exists
    try:
        player = Player.objects.get(pk=id)
    except Player.DoesNotExist:
        return HttpResponse("Sorry, this player doesn't exist!")
    # Check if the user has permission to upgrade this player
    if not player.discord_user == user:
        return HttpResponse("Sorry, you don't have permission to upgrade this player!")
    # Process the request (if it's a POST request)
    if request.method == "POST": 
        form = UpgradeForm(request.POST)
        if form.is_valid():
            response = hoops_player_upgrade.createUpgrade(player, form.cleaned_data)
            messages.success(request, response)
            return redirect(upgrade_player, id=id)
        else:
            print(form.errors)
            messages.error(request, form.errors)
            return redirect(upgrade_player, id=id)
    else:
        # Initialize the prefill information
        prefill_info = dict(player.attributes, **player.badges) # Combine the attributes & badges into one dictionary
        prefill_info = {k.lower(): v for k, v in prefill_info.items()} # To match field names in the form (lowercase)
        prefill_info = {k.replace(" ", "_"): v for k, v in prefill_info.items()} # To match field names in the form (underscores)
        # Initialize the context
        context = {
            # Context items
            "title": "Upgrade Player", 
            "player": player, 
            "upgrade_player_form": UpgradeForm(initial=prefill_info),
            "badge_attributes": prefill_info,
            "badge_prices": league_config.badge_prices,
            "attribute_prices": league_config.attribute_prices,
            # Attribute categories
            "finishing_attributes": league_config.attribute_categories["finishing"],
            "shooting_attributes": league_config.attribute_categories["shooting"],
            "playmaking_attributes": league_config.attribute_categories["playmaking"],
            "defense_attributes": league_config.attribute_categories["defense"],
            "physical_attributes": league_config.attribute_categories["physical"],
            # Badge categories
            "finishing_badges": league_config.badge_categories["finishing"],
            "shooting_badges": league_config.badge_categories["shooting"],
            "playmaking_badges": league_config.badge_categories["playmaking"],
            "defense_badges": league_config.badge_categories["defense"],
        }
        return render(request, "main/players/upgrade.html", context)

@login_required(login_url="/login/discord/")
def create_player(request):
    # Collect user & player information
    user = request.user
    # Process the request (if it's a POST request)
    if request.method == "POST": 
        form = PlayerForm(request.POST)
        if form.is_valid():
            response = hoops_player_create.validatePlayerCreation(user, form.cleaned_data)
            success = response[0]
            status = response[1]
            # If the form is valid, and the player creation succeeded, redirect to the player page
            if success == True:
                playerObject = hoops_player_create.createPlayer(user, form.cleaned_data)
                return redirect(player, id=playerObject.id)
            else:
                messages.error(request, status)
                return redirect(create_player)
        # If the form is invalid, or the player creation failed, redirect to the create player page
        return redirect(create_player)
    else:
        context = {"create_player_form": PlayerForm}
        return render(request, "main/players/create.html", context)

def players(request):
    context = {
        "title": "Players",
        "players": Player.objects.all(),
    }
    return render(request, "main/players/players.html", context)

def upgrade_logs(request, id):
    # Check if the player exists
    try:
        player = Player.objects.get(pk=id)
    except Player.DoesNotExist:
        return HttpResponse("Sorry, this player doesn't exist!")
    # Get the upgrade logs
    logs = player.history_list.history["upgrade_logs"]
    logs.reverse()
    if player:
        context = {
            "name": f"{player.first_name} {player.last_name}",
            "logs": logs,
        }
        return render(request, "main/players/history.html", context)
    else:
        return HttpResponse("Sorry, this player doesn't exist!")

def team(request, id):
    team_object = Team.objects.get(pk=id)
    context = {
        "title": team_object.name,
        "team": team_object,
    }
    return render(request, "main/teams/team.html", context)

def teams(request):
    context = {
        "title": "Teams",
        "teams": Team.objects.all(),
    }
    return render(request, "main/teams/teams.html", context)