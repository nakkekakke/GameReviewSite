# User storyt


## Nykyiset toiminnot

#### Käyttäjä pystyy kirjautumaan sisään sovellukseen

`SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.role AS account_role 
FROM account 
WHERE account.username = ? AND account.password = ? 
LIMIT 1 OFFSET 0`
 
#### Käyttäjä pystyy lisäämään pelejä arvosteluja varten

`INSERT INTO game (date_created, date_modified, name, developer, year) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)`

#### Käyttäjä pystyy tarkastelemaan lisättyjä pelejä

`SELECT game.id AS game_id, game.date_created AS game_date_created, game.date_modified AS game_date_modified, game.name AS game_name, game.developer AS game_developer, game.year AS game_year 
FROM game`

#### Käyttäjä pystyy lisäämään pelien arvosteluja

`INSERT INTO review (date_created, date_modified, content, rating, game_id, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)`

#### Käyttäjä pystyy tarkastelemaan arvosteluja

`SELECT review.id AS review_id, review.date_created AS review_date_created, review.date_modified AS review_date_modified, review.content AS review_content, review.rating AS review_rating, review.game_id AS review_game_id, review.account_id AS review_account_id 
FROM review 
WHERE ? = review.game_id`

#### Käyttäjä pystyy tarkastelemaan omia tietojaan

`SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.role AS account_role 
FROM account 
WHERE account.id = ?`

#### Adminkäyttäjä pystyy muokkaamaan pelien tietoja

`UPDATE game SET date_modified=CURRENT_TIMESTAMP, name=?, developer=?, year=? WHERE game.id = ?`

#### Adminkäyttäjä pystyy poistamaan pelejä

`DELETE FROM game WHERE game.id = ?`

#### Käyttäjä pystyy lisäämään kategorioita pelejä varten

`INSERT INTO category (date_created, date_modified, name) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?)`

#### Käyttäjä pystyy muokkaamaan omia arvostelujaan

`UPDATE review SET date_modified=CURRENT_TIMESTAMP, content=?, rating=? WHERE review.id = ?`

#### Käyttäjä pystyy poistamaan omia arvostelujaan

`DELETE FROM review WHERE review.id = ?`

#### Adminkäyttäjä pystyy muokkaamaan arvosteluja

`UPDATE review SET date_modified=CURRENT_TIMESTAMP, content=?, rating=? WHERE review.id = ?`

#### Adminkäyttäjä pystyy poistamaan arvosteluja

`DELETE FROM review WHERE review.id = ?`

#### Adminkäyttäjä pystyy poistamaan kategorioita

`DELETE FROM category WHERE category.id = ?`

## Jatkokehitysideoita

- Käyttäjä pystyy muokkaamaan omia tietojaan
- Adminkäyttäjä pystyy poistamaan normaalikäyttäjiä
