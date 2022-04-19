create database football;

## import tables 'champions.csv', 'results.csv', 'players,csv' from  "data" folder:

create temporary table wins_year(
select max(counts) as counts, year
from
(
select year, count(winner) as counts, winner
from results
where year >= 2002
and winner <> 'None'
group by year, winner) as a
group by year);


create temporary table wins_year_country(
select year, count(winner) as counts, winner
from results
where year >= 2002
and winner <> 'None'
group by year, winner);

create table winner_year(
select a.counts, a.year, b.winner from wins_year as a
join wins_year_country b on a.year=b.year and a.counts=b.counts);

-- table that has each awarded player with their club, nationality, champion league's champion of that year, and country that won most matches in that year --
select players.Year, players.Player, players.Club, players.Nationality, champions.Champion, winner_year.winner from players
join champions on champions.year=players.year
join winner_year on winner_year.year=players.year
;

-- selected best players in the world and that their team has won the most matches in the year --
select players.Year, players.Player, players.Club, players.Nationality, champions.Champion, winner_year.winner from players
join champions on champions.year=players.year
join winner_year on winner_year.year=players.year
where players.Club = champions.Champion;

-- players that won the champions league that year and were selected best in the world --
select players.Year, players.Player, players.Club, players.Nationality, champions.Champion, winner_year.winner from players
join champions on champions.year=players.year
join winner_year on winner_year.year=players.year
where players.Nationality = winner_year.winner;

-- champion players with their club in champions league, whose national team has won the most games in the year and selected best in the world -- 
select players.Year, players.Player, players.Club, players.Nationality, champions.Champion, winner_year.winner from players
join champions on champions.year=players.year
join winner_year on winner_year.year=players.year
where players.Nationality = winner_year.winner
and players.Club = champions.Champion;