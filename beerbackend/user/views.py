# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import Blueprint, flash, redirect, render_template, request, url_for
from beerbackend.utils import flash_errors


blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    return render_template('users/members.html', user=current_user, profile=current_user.get_profile(),
                           ratings=sorted(current_user.ratings, key=lambda rating: rating.created_at), str=str)



