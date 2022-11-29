/**
 * insert_node - add to list
 * @number: data
 * @head: pointer to list to be freed
 * Return: pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *curr = *head;

	if (new == NULL)
		return (NULL);
	new->n = number;
	if (number <= curr->n)
	{
		new->next = curr;
		head = &new;
		return (new);
	}

	while (curr)
	{
		if (curr->next == NULL)
		{
			curr->next = new;
			return (new);
		}
		else if (number <= curr->next->n)
		{
			new->next = curr->next;
			curr->next = new;
			return (new);
		}
		else
		{
			curr = curr->next;
		}
	}
	return (NULL);
}
