import xadmin
from xadmin import views

from spl.models import Source, Ingredient, SetInfo, ProductData, Task


class GlobalSetting(object):
    global_search_models = [Source]
    # global_models_icon = {
    #     Source: 'fa fa-laptop', Ingredient: 'fa fa-cloud'
    # }
    menu_style = 'default'  # 'accordion'
    site_title = 'Pillbox Engine'
    site_footer = 'Pillbox'
xadmin.site.register(views.CommAdminView, GlobalSetting)


class SourceAdmin(object):

    search_fields = ['title']
    reversion_enable = True

    model_icon = 'fa fa-download'


class IngredientAdmin(object):

    list_display = ('name', 'code_system', 'class_code')
    list_filter = ['code_system', 'class_code']
    list_quick_filter = ['class_code']
    search_fields = ['name']
    reversion_enable = True

    model_icon = 'fa fa-dot-circle-o'


class SetInfoAdmin(object):

    list_display = ('setid', 'title', 'source', 'version_number', 'author', 'is_osdf',
                    'effective_time', 'version_number')
    list_filter = ['version_number', 'is_osdf']
    list_quick_filter = ['is_osdf', 'source']
    search_fields = ['title', 'setid', 'author', 'author_legal', 'filename']
    reversion_enable = True

    model_icon = 'fa fa-stethoscope'


class ProductDataAdmin(object):

    fields = ['id', 'setid', 'dosage_form', 'ndc', 'ndc9', 'product_code',
              'equal_product_code', 'approval_code', 'medicine_name', 'part_num',
              'part_medicine_name', 'rxtty', 'rxstring', 'rxcui', 'dea_schedule_code',
              'dea_schedule_name', 'marketing_act_code', 'splcolor', 'splsize',
              'splshape', 'splimprint', 'splimage', 'splscore']

    readonly_fields = fields

    list_display = ('medicine_name', 'product_code', 'part_num', 'dosage_form')
    list_filter = ['product_code', 'dosage_form']
    list_quick_filter = ['splcolor', 'splsize', 'splscore']
    search_fields = ['medicine_name', 'part_medicine_name']
    reversion_enable = True

    model_icon = 'fa fa-medkit'


class TaskAdmin(object):

    def added(self, instance):
        if instance.meta:
            return instance.meta['added']
        return 0
    added.short_description = "Added"
    added.is_column = True

    def updated(self, instance):
        if instance.meta:
            return instance.meta['updated']
        return 0
    updated.short_description = "Updated"
    updated.is_column = True

    list_display = ('task_id', 'name', 'status', 'duration', 'added', 'updated', 'time_started', 'time_ended')
    fields = ['task_id', 'name', 'status', 'duration', 'time_started', 'time_ended']
    readonly_fields = ['task_id', 'name', 'status', 'duration', 'time_started', 'time_ended']

    model_icon = 'fa fa-tasks'

xadmin.site.register(Source, SourceAdmin)
xadmin.site.register(Ingredient, IngredientAdmin)
xadmin.site.register(SetInfo, SetInfoAdmin)
xadmin.site.register(ProductData, ProductDataAdmin)
xadmin.site.register(Task, TaskAdmin)
