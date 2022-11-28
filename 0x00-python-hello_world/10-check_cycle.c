#include "list.h"
/**
 * check_cycle - fun
 * @list: lol
 * Return:int
*/
int check_cycle(listint_t *list)
{
	listint_t *curr = list;

	while (curr)
	{
		if (curr->n == -444)
			return (1);
		curr->n = -444;
		curr = curr->next;
	}
	return (0);
}
