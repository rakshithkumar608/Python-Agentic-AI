def make_chai(): #this is a main function to make chai and box 
   if not kettle_has_water():
       fill_kettle_with_water()
       plug_in_kettle()
       boil_water()
       if not is_cup_clean():
           clean_cup()
           add_to_cup('tea bag')
           add_to_cup('sugar')
           pour('boiled water')
           stie("cup")
           serve("chai")


           make_chai()


