use sakila;

#Question 1
SELECT title, rating, c.name
FROM film as f INNER JOIN film_category as fc
ON f.film_id = fc.film_id
INNER JOIN category as c
ON c.category_id = fc.category_id
WHERE rating != 'PG';

#Question 2
select concat(first_name, " ", last_name) as full_name, count(film_id) as NO_of_films
from actor LEFT JOIN film_actor
ON actor.actor_id = film_actor.actor_id
GROUP BY actor.actor_id;


#Question 3
SELECT title, Count(inventory_id) as Amount_in_inventory
FROM inventory as i INNER JOIN film as f
ON i.film_id = f.film_id
GROUP BY title
ORDER BY Amount_in_inventory desc;

#Question 4
#Subquery
SELECT avg(replacement_cost) as average
FROM film
WHERE rating = 'PG'; -- 18.95

#Answer
SELECT* 
FROM film 
WHERE replacement_cost > (
SELECT avg(replacement_cost) as average
FROM film
WHERE rating = 'PG'
);