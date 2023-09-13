class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return f'Sk ok({self.ingredients!r})'
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'


    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

print(Pizza.margherita())