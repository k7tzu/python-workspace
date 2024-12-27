-- 1:
SELECT * FROM Film WHERE sortie = 1984;

-- 2:
SELECT * FROM Internaute WHERE inscription BETWEEN '2018-01-01' AND '2019-12-31';

-- 3:
SELECT titre, moyenne FROM Film WHERE duree >= 180;

-- 4:
SELECT titre FROM Film WHERE sortie > 2000 AND moyenne > 8;

-- 5:
SELECT * FROM Film
JOIN Realisateur ON Film.Realisateur = Realisateur.id_realisateur
WHERE Realisateur.nom = 'Alfred Hitchcock';

-- 6:
SELECT DISTINCT titre FROM Film
JOIN Note ON Film.id_film = Note.film
WHERE Note.points = 1;

-- 7:
SELECT Internaute.email, Note.points FROM Internaute
JOIN Note ON Internaute.id_internaute = Note.internaute
JOIN Film ON Film.id_film = Note.film
WHERE Film.titre = 'Les Profs';