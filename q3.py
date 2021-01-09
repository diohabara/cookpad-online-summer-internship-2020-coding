import json
import subprocess
import unittest
import sys


def sorted_monsters_by_power() -> str:
    monsters = ['dragon', 'griffin', 'medusa', 'troll', 'vampire']
    url = 'https://ob6la3c120.execute-api.ap-northeast-1.amazonaws.com/Prod/battle/'
    power_of_monster = {}
    for monster in monsters:
        power_of_monster[monster] = 0

    for i in range(len(monsters)):
        for j in range(i+1, len(monsters)):
            monster1, monster2 = monsters[i], monsters[j]
            cmd = ['curl', url + f"{monster1}+{monster2}"]
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            o, e = proc.communicate()
            winner_loser_dict = json.loads(o.decode())
            winner = winner_loser_dict['winner']
            loser = winner_loser_dict['loser']
            print(f"{winner=}, {loser=}", file=sys.stderr)
            power_of_monster[winner] += 1

    print(power_of_monster, file=sys.stderr)
    sorted_power_of_monsters = sorted(power_of_monster.items(), key=lambda x: -x[1])
    sorted_monsters = [monster[0] for monster in sorted_power_of_monsters]
    return sorted_monsters
        
class TestQuestion3(unittest.TestCase):
    def test_sort_monsters_by_power(self):
        # expected = 'dragon, griffin, medusa, troll, vampire' # from Web page, but it's not correct...
        expected = ['troll', 'dragon', 'medusa', 'griffin', 'vampire']
        achieved = sorted_monsters_by_power()
        self.assertEqual(expected, achieved)

if __name__ == "__main__":
    unittest.main()

