from django.urls import path
from . import views

urlpatterns = [
    # Home & login PATHS
    path(route="", view=views.home, name="home"),
    path(route="login/", view=views.login, name="login"),
    path(route="login/discord/", view=views.login_discord, name="login_discord"),
    path(
        route="login/discord/redirect/",
        view=views.login_discord_redirect,
        name="login_discord_redirect",
    ),
    path(route="logout/", view=views.logout, name="logout"),
    # Player PATHS
    path(route="player/<int:id>/", view=views.player, name="player"),
    path(
        route="player/upgrade/<int:id>/",
        view=views.upgrade_player,
        name="upgrade_player",
    ),
    path(route="player/create/", view=views.create_player, name="create_player"),
    path(route="players/", view=views.players, name="players"),
    path(route="logs/upgrades/<int:id>/", view=views.upgrade_logs, name="upgrade_logs"),
    path(
        route="players/archetype-traits/",
        view=views.archetype_traits,
        name="archetype_traits",
    ),
    path(
        route="players/build-info/<str:tag>/", view=views.build_info, name="build_info"
    ),
    # Team PATHS
    path(route="team/<int:id>/", view=views.team, name="team"),
    path(route="teams/", view=views.teams, name="teams"),
    path(route="team/trade/", view=views.trade, name="trade"),
    # Misc PATHS
    path(
        route="upgrades/pending/", view=views.upgrades_pending, name="upgrades_pending"
    ),
    # Check PATHS
    path(
        route="players/search/",
        view=views.check_player_search,
        name="check_player_search",
    ),
]
