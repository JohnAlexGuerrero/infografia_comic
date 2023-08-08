from django.contrib import admin

from characters.models import Character#, Abilities, Weapon, Profession

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',)


# @admin.register(Abilities)
# class AbilitiesAdmin(admin.ModelAdmin):
#     list_display = ('name',)
    
# @admin.register(Weapon)
# class WeaponAdmin(admin.ModelAdmin):
#     list_display = ('name',)
    
# @admin.register(Profession)
# class ProfessionAdmin(admin.ModelAdmin):
#     list_display = ('name',)


