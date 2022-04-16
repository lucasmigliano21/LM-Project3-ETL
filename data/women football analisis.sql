create database football;

select * from df2
limit 100;

create temporary table wins_year(
select max(counts) as counts, year
from
(
select year, count(winner) as counts, winner
from df2
where year >= 2002
and winner <> 'None'
group by year, winner) as a
group by year);


create temporary table wins_year_country(
select year, count(winner) as counts, winner
from df2
where year >= 2002
and winner <> 'None'
group by year, winner);

create  table winner_year(
select a.counts, a.year, b.winner from wins_year as a
join wins_year_country b on a.year=b.year and a.counts=b.counts);


select * from winner_year;

select * from players;

select * from champions;

-- la posta--
select players.Year, players.Player, players.Club, players.Nationality, champions.Champion, winner_year.winner from players
join champions on champions.year=players.year
join winner_year on winner_year.year=players.year
;

-- jugadoras seleccionadas mejores del mundo y que su seleccion haya ganado la mayor cantidad de partidos en el año --
select players.Year, players.Player, players.Club, players.Nationality, champions.Champion, winner_year.winner from players
join champions on champions.year=players.year
join winner_year on winner_year.year=players.year
where players.Club = champions.Champion;

-- jugadoras campeonas con su club en champions y seleccionadas mejores del mundo --
select players.Year, players.Player, players.Club, players.Nationality, champions.Champion, winner_year.winner from players
join champions on champions.year=players.year
join winner_year on winner_year.year=players.year
where players.Nationality = winner_year.winner;

-- jugadoras campeonas con su club en champions, cuya seleccion haya ganado la mayor cantidad de partidos en el año y seleccionadas mejores del mundo -- 
select players.Year, players.Player, players.Club, players.Nationality, champions.Champion, winner_year.winner from players
join champions on champions.year=players.year
join winner_year on winner_year.year=players.year
where players.Nationality = winner_year.winner
and players.Club = champions.Champion;