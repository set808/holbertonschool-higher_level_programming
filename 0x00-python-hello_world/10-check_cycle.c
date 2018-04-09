#include "lists.h"
/**
 * check_cycle - checks a linked list for a cycle
 * @list: head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *one, *two;

	one = list;
	two = list;

	if (!list)
		return (0);
	
	while (one && two)
	{
		one = one->next;
		if (two->next)
			two = two->next->next;
		if (one == two)
			return (1);
	}
	return (0);
}
