
from flask_login import login_required, current_user
from beerbackend.beer.forms import BeerForm
from flask import Blueprint, flash, redirect, render_template, request, url_for
from beerbackend.utils import flash_errors
from beerbackend.beer.models import Beer


blueprint = Blueprint('beer', __name__, url_prefix='/beers', static_folder='../static')

@blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BeerForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            Beer.create(beer_name=form.beer_name.data, abv=form.abv.data, hoppiness=form.hoppiness.data,
                        bitterness=form.bitterness.data, fruitiness=form.bitterness.data)
            flash('You added a beer: success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('beers/addbeer.html', form=form)

@blueprint.route('/', methods=['GET'])
def all():
    beers = Beer.query.all()
    return render_template('beers/all.html', beers=beers)
