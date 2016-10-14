
from flask_login import login_required, current_user
from beerbackend.beer.forms import BeerForm
from flask import Blueprint, flash, redirect, render_template, request, url_for
from beerbackend.utils import flash_errors
from beerbackend.beer.models import Beer
from flask_restful import Resource, Api, reqparse, fields, marshal_with


blueprint = Blueprint('beer', __name__, url_prefix='/beers', static_folder='../static')




@blueprint.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = BeerForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            Beer.create(beer_name=form.beer_name.data, abv=form.abv.data, bitter=form.bitter.data,
                        color=form.color.data, fruit=form.fruit.data, hoppy=form.hoppy.data, malty=form.malty.data,
                        roasty=form.roasty.data, smoke=form.smoke.data, sour=form.sour.data,
                        spice=form.spice.data,
                        sweet=form.sweet.data, wood=form.wood.data, family=form.family.data)

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
