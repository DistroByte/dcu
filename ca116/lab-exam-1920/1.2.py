#!/usr/bin/env python3

home_goals = 1
home_points = 2
away_goals = 0
away_points = 6

home_score = (home_goals * 7) + home_points
away_score = (away_goals * 7) + away_points

if home_score < away_score:
    print("away win")
elif away_score < home_score:
    print("home win")
else:
    print("draw")
