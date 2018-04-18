#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the first node of linked list
 *
 * Return: returns 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	unsigned int x, y, half, opp;
	listint_t *runner, *runner2;

	if(!*head)
		return (1);
	x = 0;
	runner = *head;
	runner2 = *head;
	while (runner->next)
	{
		runner = runner->next;
		x++;
	}
	if (runner->n != (*head)->n)
		return (0);
	if (x == 1)
		return (1);

	half = x / 2;
	opp = x - 2;

	x = 0;
	while (x < half)
	{
		runner2 = runner2->next;
		runner = runner2;
		for (y = 0; y < opp; y++)
			runner = runner->next;
		if (runner2->n != runner->n)
			return (0);
		x++;
		opp -= 2;
	}
	return (1);
}
