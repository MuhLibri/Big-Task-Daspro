def save_F04 (lines):
    g=open("store_game.csv", 'a')
    g.writelines(lines)
    g.close()
   
def save_F05_F06_ (unChanged_line,Changed_line) :
    g=open("store_game.csv", 'w')
    g.writelines(unChanged_line)
    g.close()
    g=open("store_game.csv", 'a')
    g.writelines(Changed_line)
    g.close()
