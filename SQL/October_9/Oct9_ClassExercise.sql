use sakila;

#Question 1
select customer_id, count(rental_id) as rental_amount 
from rental
GROUP BY customer_id
ORDER BY rental_amount desc
LIMIT 5;

SELECT customer.customer_id, CONCAT(first_name, " ", last_name) as full_name, count(rental_id) as rental_amount
FROM rental INNER JOIN customer
ON rental.customer_id = customer.customer_id
GROUP BY customer_id
ORDER BY rental_amount desc
LIMIT 5;

#Question 2
SELECT district, count(address) as NO_of_Addresses
FROM address
GROUP BY district
ORDER BY NO_of_addresses desc;

#Question 3
SELECT title, rental_rate, replacement_cost
FROM film
WHERE rental_rate < 1 OR replacement_cost < 15;


#Question 4
SELECT customer_id, SUM(amount) as "total amount spent"
FROM payment
GROUP BY customer_id
HAVING SUM(amount) >= 150;

SELECT customer.customer_id, CONCAT(first_name, " ", last_name) as full_name, SUM(amount) as "total amount spent"
FROM payment INNER JOIN customer
ON payment.customer_id = customer.customer_id
GROUP BY customer_id
HAVING SUM(amount) >= 150;

#Question 5
SELECT customer_id, first_name
FROM customer
WHERE first_name LIKE '%__o';

#Merging question 1 and 4
CREATE VIEW amount_rented AS 
SELECT customer.customer_id, CONCAT(first_name, " ", last_name) as full_name, count(rental_id) as rental_amount
FROM rental INNER JOIN customer
ON rental.customer_id = customer.customer_id
GROUP BY customer_id
ORDER BY rental_amount desc;

SELECT payment.customer_id, full_name, SUM(amount) as "total amount spent",  rental_amount
FROM amount_rented INNER JOIN payment
ON payment.customer_id = amount_rented.customer_id
GROUP BY payment.customer_id;
