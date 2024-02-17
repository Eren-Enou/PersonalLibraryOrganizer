# File: app/routes/dashboard.py

from flask import render_template, request, redirect, url_for
from app import app
from flask_login import login_required

from app.forms import MangaSearchForm
from app.mangadex_api import MangaDexAPI

@app.route('/dashboard')
@login_required
def dashboard():
    # Your logic to fetch user-specific data goes here
    return render_template('dashboard.html')

@app.route('/dashboard/search', methods=['GET', 'POST'])
@login_required
def manga_search():
    form = MangaSearchForm()
    form.tag_choices.choices = MangaSearchForm.generate_tag_choices()  # Set dynamic choices
    
    if form.validate_on_submit():
        mangadex_api = MangaDexAPI()
        
        # Accessing form data
        title_query = form.title_query.data
        included_tags = request.form.get('included_tag_names', '').split(',')
        excluded_tags = request.form.get('excluded_tag_names', '').split(',')
        sort_by = form.sort_by.data
        limit = form.limit.data
        
        included_tags = [tag for tag in included_tags if tag]
        excluded_tags = [tag for tag in excluded_tags if tag]
        
        publication_demographic = form.publication_demographic.data
        status = form.status.data
        content_rating = form.content_rating.data
        
        # Prepare filters for the API call
        filters = {}
        if publication_demographic:
            filters["publicationDemographic[]"] = publication_demographic
        if status:
            filters["status[]"] = status
        if content_rating:
            filters["contentRating[]"] = content_rating
        
        print("status:",status)
        # Assuming your API class can handle empty lists for tags correctly
        results = mangadex_api.search_manga(
            limit=limit,
            title=title_query,
            included_tag_names=included_tags,
            excluded_tag_names=excluded_tags,
            sort_by=sort_by,
            **filters
        )
        
        # Process results to include additional data as needed
        # For example, fetching cover art if not already included in search results
        
        return render_template('search_results.html', results=results['data'])
    
    return render_template('search_form.html', form=form)