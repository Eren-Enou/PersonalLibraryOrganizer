# File: app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, IntegerField, SubmitField
from wtforms.validators import Optional


class MangaSearchForm(FlaskForm):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('hiatus', 'Hiatus'), 
        ('cancelled', 'Cancelled')
    ]
    DEMOGRAPHIC_CHOICES = [
        ('shounen', 'Shounen'),
        ('shoujo', 'Shoujo'), 
        ('seinen', 'Seinen'), 
        ('josei', 'Josei')

    ]
    CONTENT_RATING_CHOICES = [
        ('safe', 'Safe'),
        ('suggestive', 'Suggestive'), 
        ('erotica', 'Erotica'), 
        ('pornographic', 'Pornographic')
    ]
    SORT_CHOICES = [
        ('relevance_desc', 'Best Match'),  # Assuming relevance is the default sort option
        ('latestUploadedChapter_desc', 'Latest Upload'),
        ('latestUploadedChapter_asc', 'Oldest Upload'),
        ('title_asc', 'Title Ascending'),
        ('title_desc', 'Title Descending'),
        ('rating_desc', 'Highest Rating'),  # Assuming rating is the correct field name
        ('rating_asc', 'Lowest Rating'),
        ('followedCount_desc', 'Most Follows'),
        ('followedCount_asc', 'Fewest Follows'),
        ('createdAt_desc', 'Recently Added'),
        ('createdAt_asc', 'Oldest Added'),
        ('year_asc', 'Year Ascending'),
        ('year_desc', 'Year Descending'),
    ]
    
    @staticmethod
    def generate_tag_choices():
        # Static dictionary for tags
        ALL_TAGS = {
            'Genre': ['Action', 'Adventure', "Boys' Love", 'Comedy', 'Crime', 'Drama', 'Fantasy', "Girls' Love", 'Historical', 'Horror', 'Isekai', 'Magical Girls', 'Mecha', 'Medical', 'Mystery', 'Philosophical', 'Psychological', 'Romance', 'Sci-Fi', 'Slice of Life', 'Sports', 'Superhero', 'Thriller', 'Tragedy', 'Wuxia'],
            'Theme': ['Aliens', 'Animals', 'Cooking', 'Crossdressing', 'Delinquents', 'Demons', 'Genderswap', 'Ghosts', 'Gyaru', 'Harem', 'Incest', 'Loli', 'Mafia', 'Magic', 'Martial Arts', 'Military', 'Monster Girls', 'Monsters', 'Music', 'Ninja', 'Office Workers', 'Police', 'Post-Apocalyptic', 'Reincarnation', 'Reverse Harem', 'Samurai', 'School Life', 'Shota', 'Supernatural', 'Survival', 'Time Travel', 'Traditional Games', 'Vampires', 'Video Games', 'Villainess', 'Virtual Reality', 'Zombies']
        }
        # Flatten the tag choices for the form field
        return [(tag, tag) for category, tags in ALL_TAGS.items() for tag in tags]
    
    title_query = StringField('Title', validators=[Optional()])
    tag_choices = SelectMultipleField('Tags', choices=[], validators=[Optional()])
    included_tag_names = StringField('Include Tags', validators=[Optional()])
    excluded_tag_names = StringField('Exclude Tags', validators=[Optional()])
    sort_by = SelectField('Sort by', choices=SORT_CHOICES, validators=[Optional()])
    publication_demographic = SelectMultipleField('Publication Demographic', choices=DEMOGRAPHIC_CHOICES, validators=[Optional()])
    status = SelectMultipleField('Status', choices=STATUS_CHOICES, validators=[Optional()])
    content_rating = SelectMultipleField('Content Rating', choices=CONTENT_RATING_CHOICES, validators=[Optional()])
    limit = IntegerField('Number of Results', validators=[Optional()], default=10)
    submit = SubmitField('Search')