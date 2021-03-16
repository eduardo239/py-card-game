primary = '#1F2C41'
white = '#ffffff'
dark = '#2c2c2c'
light_grey = '#ddd'
green = 'green'

group_box = f"""padding: 0;"""

lbl_simple = f"""
  font-size: 12pt;
  color: {dark};
  letter-spacing: 1px;"""

lbl_fight_stats = f"""color: {dark}; padding: 5px;"""

# btn
btn_dark = f"""
  background-color: #141414;
  color: #eef0f2;
  border: 0;
  padding: 8px 16px;
  font-style: uppercase;
  letter-spacing: 1px;"""

btn_secondary = f"""background-color: #ffffff;
  color: #011638;
  border: 0;
  padding: 8px 16px;
  font-style: uppercase;
  letter-spacing: 1px;
"""
lbl_winner = f"""font-size: 27pt; font-weight: bold; color: {green}"""
lbl_score = f"""font-size: 27pt; color: {dark}"""
lbl_stats = f"""font-size: 12pt; border: 1px solid {light_grey}; 
background-color: transparent; padding: 5px 10px; background-color: {white}"""
lbl_player_score = f"""font-size: 16pt; padding: 5px 10px;
background-color: transparent; color: {primary}; border: 1px solid {light_grey}"""

btn_primary = f"""background-color: #eec643;
  color: #141414;
  border: 0;
  padding: 5px 15px;
  font-style: uppercase;
  letter-spacing: 1px;"""

general = "QPushButton:pressed { background-color: red; border: 4px solid red; }"
