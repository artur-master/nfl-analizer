from django import template

from general.models import *

register = template.Library()

@register.filter
def div(val, de):
    if not de:
        return '-'
    return '{:.2f}'.format(val * 1.0 / de)

@register.filter
def div_pcnt(val, de):
    if not de:
        return '0.0'
    return '{:.2f}'.format(val * 100.0 / de)

@register.filter
def lstgm(team_stat):
    val = team_stat['l_pya'] + team_stat['l_ruya']
    return '{:.1f}'.format(val)

@register.filter
def hgms(team_stat):
    val = team_stat['h_pya'] + team_stat['h_ruya']
    return '{:.1f}'.format(val)

@register.filter
def agms(team_stat):
    val = team_stat['a_pya'] + team_stat['a_ruya']
    return '{:.1f}'.format(val)

@register.filter
def tyda(team_stat):
    val = team_stat['pyda'] + team_stat['ruyda']
    return '{:.1f}'.format(val)

@register.filter
def tya(team_stat):
    val = team_stat['pya'] + team_stat['ruya']
    return '{:.1f}'.format(val)

@register.filter
def pdiff_color(team_stat):
    a_val = team_stat['pyda'] + team_stat['ruyda']
    s_val = team_stat['pya'] + team_stat['ruya']

    return 'text-danger' if a_val < s_val else 'text-success'

@register.filter
def pdiff(team_stat):
    a_val = team_stat['pyda'] + team_stat['ruyda']
    s_val = team_stat['pya'] + team_stat['ruya']

    val = a_val - s_val
    fm = '{:.1f}' if val > 0 else '({:.1f})'
    return fm.format(abs(val))

@register.filter
def pdiff_pt_color(team_stat):
    a_val = team_stat['pa']
    s_val = team_stat['ps']

    return 'text-danger' if a_val < s_val else 'text-success'

@register.filter
def pdiff_pt(team_stat):
    val = team_stat['pa'] - team_stat['ps']
    fm = '{:.1f}' if val > 0 else '({:.1f})'
    return fm.format(abs(val))

@register.filter
def aya(player):
    if not player.pass_att:
        return '0.0'
    return '{:.2f}'.format((player.pass_yds + 20 * player.pass_td  - 45 * player.pass_int) * 1.0 / player.pass_att)

@register.filter()
def liked(uid, session):
    fav = session.get('fav', [])
    return 'done' if str(uid) in fav else ''

@register.filter 
def hot_sfp(player):
    if player['sfp'] >= player['afp'] + 5:
        return 'text-danger font-weight-bold'  
    elif player['sfp'] <= player['afp'] - 5:
        return 'text-primary font-weight-bold'
    else:
        return '' 

@register.filter
def ou_ml(game, team):
    if not game.ml:
        return ''

    if team in game.ml:
        return '( {} )'.format(game.ml.split(' ')[-1])
    else:
        return '( {} )'.format(int(game.ou))

@register.filter
def sgr(s):
    return s.split(' ')[0]

@register.filter
def team(opponent):
    return opponent.strip('@')

@register.filter
def vs(opponent):
    return '@' if '@' in opponent else 'vs'

@register.filter
def cus_proj(player, session):
    cus_proj = session.get('cus_proj', {})
    return cus_proj.get(str(player.id), player.proj_points)
