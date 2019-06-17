from django.contrib import admin
from mutation.models import Autosome, Auto_Mutation, Auto_Syndrome, Allo_Mutation, Allo_Syndrome

class Auto_SyndromeAdmin(admin.ModelAdmin):
    list_display = ('auto_syn_name', 'auto_syn_fre')
    ordering = ['auto_syn_name']

class Auto_MutationAdmin(admin.ModelAdmin):
    list_display = ('auto_pri', 'mutation_type', 'auto_sec', 'auto_syn_id')
    ordering = ['auto_pri']

class Allo_SyndromeAdmin(admin.ModelAdmin):
    list_display = ('allo_syn_name', 'allo_syn_fre')
    ordering = ['allo_syn_name']

class Allo_MutationAdmin(admin.ModelAdmin):
    list_display = ('linked', 'allo_syn_id')
    ordering = ['linked']

admin.site.register(Autosome)
admin.site.register(Auto_Syndrome, Auto_SyndromeAdmin)
admin.site.register(Auto_Mutation, Auto_MutationAdmin)
admin.site.register(Allo_Syndrome, Allo_SyndromeAdmin)
admin.site.register(Allo_Mutation, Allo_MutationAdmin)
