#include "lists.h"
/**
 * insert_node - inserts new value into a sorted list
 * @head: pointer to the first node of list
 * @number: new value
 * Return: returns the address of the new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *runner;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
	}

	runner = (*head)->next;
	while (runner->next != NULL)
	{
		if (runner->n <=  new->n && runner->next->n >= new->n )
		{
			new->next = runner->next;
			runner->next = new;
			return (new);
		}
		runner = runner->next;
	}
	runner->next = new;
	return (new);

}
