from libqtile import widget, bar, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy

def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/power")


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄


screens = [

    Screen(
        wallpaper='/home/pramod/Pictures/Wallpapers/Aesthetic2.png',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.Spacer(length=15,
                    background='#282738',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1":power},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                ),


                widget.GroupBox(
                    fontsize=16,
                    borderwidth=3,
                    highlight_method='block',
                    active='#E5B9C6',
                    block_highlight_text_color="#CFB3E5",
                    highlight_color='#4B427E',
                    inactive='#282738',
                    foreground='#4B427E',
                    background='#353446',
                    this_current_screen_border='#353446',
                    this_screen_border='#353446',
                    other_current_screen_border='#353446',
                    other_screen_border='#353446',
                    urgent_border='#353446',
                    rounded=True,
                    disable_drag=True,
                 ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/1.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/layout.png',
                    background="#353446"
                ),


                widget.CurrentLayout(
                    background='#353446',
                    foreground='#E5B9C6',
                    fmt='{}',
                    font="JetBrainsMonoNerdFont Bold",
                    fontsize=13,
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/search.png',
                    margin=2,
                    background='#282738',
                    mouse_callbacks={"Button1": search},
                ),

                widget.TextBox(
                    fmt='Search',
                    background='#282738',
                    font="JetBrainsMonoNerdFont Bold",
                    fontsize=13,
                    foreground='#E5B9C6',
                    mouse_callbacks={"Button1": search},
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/4.png',
                ),


                widget.WindowName(
                    background = '#353446',
                    format = "{name}",
                    font="JetBrainsMonoNerdFont Bold",
                    fontsize=13,
                    foreground='#E5B9C6',
                    empty_group_string = 'Desktop',

                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/3.png',
                ),


                widget.Systray(
                    background='#282738',
                    fontsize=2,
                ),


                widget.TextBox(
                    text=' ',
                    background='#282738',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/6.png',
                    background='#353446',
                ),


                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop1.png',
                # ),

                # widget.Net(
                # format=' {up}   {down} ',
                # background='#353446',
                # foreground='#E5B9C6',
                # font="JetBrains Mono Bold",
                # prefix='k',
                # ),

                # widget.Image(
                    # filename='~/.config/qtile/Assets/2.png',
                # ),

                # widget.Spacer(
                    # length=8,
                    # background='#353446',
                # ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/ram.png',
                    background='#353446',
                ),


                widget.Spacer(
                    length=-7,
                    background='#353446',
                ),


                widget.Memory(
                    background='#353446',
                    format='{MemUsed: .0f}{mm}',
                    foreground='#E5B9C6',
                    font="JetBrainsMonoNerdFont Bold",
                    fontsize=13,
                    update_interval=5,
                    mouse_callbacks={
                        'Button1': lazy.group['scratchpad'].dropdown_toggle('htop'),
                    }
                ),

    
                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop2.png',
                # ),



                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                widget.BatteryIcon(
                    theme_path='~/.config/qtile/Assets/Battery/',
                    background='#353446',
                    scale=1,
                ),


                widget.Battery(
                    font="JetBrainsMonoNerdFont Bold",
                    fontsize=13,
                    background='#353446',
                    foreground='#E5B9C6',
                    format='{percent:2.0%}',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#353446',
                ),


                # widget.Battery(format=' {percent:2.0%}',
                    # font="JetBrains Mono Bold",
                    # fontsize=12,
                    # padding=10,
                    # background='#353446',
                # ),

                # widget.Memory(format='﬙{MemUsed: .0f}{mm}',
                    # font="JetBrains Mono Bold",
                    # fontsize=12,
                    # padding=10,
                    # background='#4B4D66',
                # ),

                widget.Volume(
                    font="JetBrainsMonoNerdFont Bold",
                    fontsize=13,
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    background='#353446',
                    # Commands to get volume and mute status
                    get_volume_command='pactl get-sink-volume @DEFAULT_SINK@ | awk \'{print $5}\'',
                    get_muted_command='pactl get-sink-mute @DEFAULT_SINK@ | awk \'{print $2}\'',
                    volume_app='pactl set-sink-volume @DEFAULT_SINK@ {{}}%',
                    mute_app='pactl set-sink-mute @DEFAULT_SINK@ toggle',
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle'),  # Toggle mute
                        'Button4': lambda: qtile.cmd_spawn('pactl set-sink-volume @DEFAULT_SINK@ +5%'),  # Increase volume
                        'Button5': lambda: qtile.cmd_spawn('pactl set-sink-volume @DEFAULT_SINK@ -5%'),  # Decrease volume
                    }
                ),


                widget.Spacer(
                    length=-5,
                    background='#353446',
                    ),


                widget.Volume(
                    font="JetBrainsMonoNerdFont Bold",
                    fontsize=13,
                    background='#353446',
                    foreground='#E5B9C6',
                    # Commands to get volume and mute status
                    get_volume_command='pactl get-sink-volume @DEFAULT_SINK@ | awk \'{print $5}\'',
                    get_muted_command='pactl get-sink-mute @DEFAULT_SINK@ | awk \'{print $2}\'',
                    volume_app='pactl set-sink-volume @DEFAULT_SINK@ {{}}%',
                    mute_app='pactl set-sink-mute @DEFAULT_SINK@ toggle',
                    mouse_callbacks={
                        'Button1': lambda: qtile.cmd_spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle'),  # Toggle mute
                        'Button4': lambda: qtile.cmd_spawn('pactl set-sink-volume @DEFAULT_SINK@ +5%'),  # Increase volume
                        'Button5': lambda: qtile.cmd_spawn('pactl set-sink-volume @DEFAULT_SINK@ -5%'),  # Decrease volume
                    }
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/5.png',
                    background='#353446',
                ),


                widget.Image(
                    filename='~/.config/qtile/Assets/Misc/clock.png',
                    background='#282738',
                    margin_y=6,
                    margin_x=5,
                ),


                widget.Clock(
                    format='%I:%M %p',
                    background='#282738',
                    foreground='#E5B9C6',
                    font="JetBrainsMonoNerdFont Bold",
                    fontsize=13,
                ),


                widget.Spacer(
                    length=18,
                    background='#282738',
                ),

                widget.TextBox(
                    "",
                    fontsize=22,
                    background="#282738",
                    foreground="#CAA9E0",
                    padding=4,
                ),
                widget.Clock(
                    format=" %a %b %d",
                    background="#282738",
                    foreground="#E5B9C6",
                    font="JetBrainsMonoNerdFont Bold",
                    fontsize=13,
                ),

                widget.Spacer(
                    length=18,
                    background='#282738',
                ),


            ],
            30,
            border_color = '#282738',
            border_width = [0,0,0,0],
            margin = [10,15,0,15],

        ),
    ),
]

