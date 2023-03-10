from django import forms
from .league import config as league_config


class PlayerForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=16)
    last_name = forms.CharField(label="Last Name", max_length=16)
    height = forms.ChoiceField(label="Height", choices=league_config.height_choices)
    weight = forms.IntegerField(
        label="Weight",
        min_value=league_config.player_weight_min,
        max_value=league_config.player_weight_max,
    )
    primary_position = forms.ChoiceField(
        label="Primary Position", choices=league_config.position_choices
    )
    secondary_position = forms.ChoiceField(
        label="Secondary Position", choices=league_config.position_choices
    )
    jersey_number = forms.IntegerField(
        label="Jersey Number", min_value=0, max_value=league_config.max_attribute
    )


class UpgradeForm(forms.Form):
    # Attributes
    driving_layup = forms.IntegerField(
        label="Driving Layup",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    post_fadeaway = forms.IntegerField(
        label="Post Fadeaway",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    post_hook = forms.IntegerField(
        label="Post Hook",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    post_control = forms.IntegerField(
        label="Post Control",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    draw_foul = forms.IntegerField(
        label="Draw Foul",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    shot_close = forms.IntegerField(
        label="Shot Close",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    mid_range_shot = forms.IntegerField(
        label="Mid Range Shot",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    three_point_shot = forms.IntegerField(
        label="Three Point Shot",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    free_throw = forms.IntegerField(
        label="Free Throw",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    ball_control = forms.IntegerField(
        label="Ball Control",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    passing_iq = forms.IntegerField(
        label="Passing Iq",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    passing_vision = forms.IntegerField(
        label="Passing Vision",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    passing_accuracy = forms.IntegerField(
        label="Passing Accuracy",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    defensive_rebound = forms.IntegerField(
        label="Defensive Rebound",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    offensive_rebound = forms.IntegerField(
        label="Offensive Rebound",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    standing_dunk = forms.IntegerField(
        label="Standing Dunk",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    driving_dunk = forms.IntegerField(
        label="Driving Dunk",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    shot_iq = forms.IntegerField(
        label="Shot Iq",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    interior_defense = forms.IntegerField(
        label="Interior Defense",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    perimeter_defense = forms.IntegerField(
        label="Perimeter Defense",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    block = forms.IntegerField(
        label="Block",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    steal = forms.IntegerField(
        label="Steal",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    shot_contest = forms.IntegerField(
        label="Shot Contest",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    lateral_quickness = forms.IntegerField(
        label="Lateral Quickness",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    hands = forms.IntegerField(
        label="Hands",
        min_value=league_config.start_attribute,
        max_value=league_config.max_attribute,
        widget=forms.NumberInput(attrs={"onchange": "updatePrice()"}),
    )
    # Physicals
    # speed = forms.IntegerField(disabled=True, label="Speed", min_value=league_config.start_attribute, max_value=league_config.max_attribute)
    # speed_with_ball = forms.IntegerField(disabled=True, label="Speed With Ball", min_value=league_config.start_attribute, max_value=league_config.max_attribute)
    # acceleration = forms.IntegerField(disabled=True, label="Acceleration", min_value=league_config.start_attribute, max_value=league_config.max_attribute)
    # vertical = forms.IntegerField(disabled=True, label="Vertical", min_value=league_config.start_attribute, max_value=league_config.max_attribute)
    # strength = forms.IntegerField(disabled=True, label="Strength", min_value=league_config.start_attribute, max_value=league_config.max_attribute)
    # Badges
    acrobat = forms.ChoiceField(
        label="Acrobat",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    aerial_wizard = forms.ChoiceField(
        label="Aerial Wizard",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    backdown_punisher = forms.ChoiceField(
        label="Backdown Punisher",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    bully = forms.ChoiceField(
        label="Bully",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    dream_shake = forms.ChoiceField(
        label="Dream Shake",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    drop_stepper = forms.ChoiceField(
        label="Drop Stepper",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    fast_twitch = forms.ChoiceField(
        label="Fast Twitch",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    fearless_finisher = forms.ChoiceField(
        label="Fearless Finisher",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    giant_slayer = forms.ChoiceField(
        label="Giant Slayer",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    limitless_takeoff = forms.ChoiceField(
        label="Limitless Takeoff",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    masher = forms.ChoiceField(
        label="Masher",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    post_spin_technician = forms.ChoiceField(
        label="Post Spin Technician",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    posterizer = forms.ChoiceField(
        label="Posterizer",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    pro_touch = forms.ChoiceField(
        label="Pro Touch",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    rise_up = forms.ChoiceField(
        label="Rise Up",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    slithery = forms.ChoiceField(
        label="Slithery",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    agent_threes = forms.ChoiceField(
        label="Agent 3",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    amped = forms.ChoiceField(
        label="Amped",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    blinders = forms.ChoiceField(
        label="Blinders",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    catch_and_shoot = forms.ChoiceField(
        label="Catch and Shoot",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    claymore = forms.ChoiceField(
        label="Claymore",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    corner_specialist = forms.ChoiceField(
        label="Corner Specialist",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    deadeye = forms.ChoiceField(
        label="Deadeye",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    green_machine = forms.ChoiceField(
        label="Green Machine",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    guard_up = forms.ChoiceField(
        label="Guard Up",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    limitless_range = forms.ChoiceField(
        label="Limitless Range",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    middy_magician = forms.ChoiceField(
        label="Middy Magician",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    slippery_off_ball = forms.ChoiceField(
        label="Slippery Off Ball",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    space_creator = forms.ChoiceField(
        label="Space Creator",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    volume_shooter = forms.ChoiceField(
        label="Volume Shooter",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    ankle_breaker = forms.ChoiceField(
        label="Ankle Breaker",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    bail_out = forms.ChoiceField(
        label="Bail Out",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    break_starter = forms.ChoiceField(
        label="Break Starter",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    clamp_breaker = forms.ChoiceField(
        label="Clamp Breaker",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    killer_combos = forms.ChoiceField(
        label="Killer Combos",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    dimer = forms.ChoiceField(
        label="Dimer",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    floor_general = forms.ChoiceField(
        label="Floor General",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    handles_for_days = forms.ChoiceField(
        label="Handles for Days",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    hyperdrive = forms.ChoiceField(
        label="Hyperdrive",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    mismatch_expert = forms.ChoiceField(
        label="Mismatch Expert",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    needle_threader = forms.ChoiceField(
        label="Needle Threader",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    post_playmaker = forms.ChoiceField(
        label="Post Playmaker",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    quick_first_step = forms.ChoiceField(
        label="Quick First Step",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    special_delivery = forms.ChoiceField(
        label="Special Delivery",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    unpluckable = forms.ChoiceField(
        label="Unpluckable",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    vice_grip = forms.ChoiceField(
        label="Vice Grip",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    anchor = forms.ChoiceField(
        label="Anchor",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    ankle_braces = forms.ChoiceField(
        label="Ankle Braces",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    challenger = forms.ChoiceField(
        label="Challenger",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    chase_down_artist = forms.ChoiceField(
        label="Chase Down Artist",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    clamps = forms.ChoiceField(
        label="Clamps",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    glove = forms.ChoiceField(
        label="Glove",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    interceptor = forms.ChoiceField(
        label="Interceptor",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    menace = forms.ChoiceField(
        label="Menace",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    off_ball_pest = forms.ChoiceField(
        label="Off Ball Pest",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    pick_dodger = forms.ChoiceField(
        label="Pick Dodger",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    post_lockdown = forms.ChoiceField(
        label="Post Lockdown",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    pogo_stick = forms.ChoiceField(
        label="Pogo Stick",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    work_horse = forms.ChoiceField(
        label="Work Horse",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    brick_wall = forms.ChoiceField(
        label="Brick Wall",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    boxout_beast = forms.ChoiceField(
        label="Boxout Beast",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )
    rebound_chaser = forms.ChoiceField(
        label="Rebound Chaser",
        choices=league_config.badge_upgrade_choices,
        widget=forms.Select(attrs={"onchange": "updatePrice()"}),
    )