function updateElementIndex(el, prefix, ndx) {
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function addForm(btn, prefix) {
    var formCount = parseInt($('#id_' + prefix + '-TOTAL_FORMS').val());
    var row = $('.dynamic-form-adder').clone(true).get(0);
    //change the cloned row class name
    var brand_tr_class_name = $(row).attr('class');
    $(row).removeClass(brand_tr_class_name);
    $(row).addClass('dynamic-form');
    //insert into the table as the last element
    $(row).removeAttr('id');
    $(row).removeAttr('style');
    //replace the empty form __prefix__ with the actual form number count
    var replace_prefix = $(row).html().replace(/__prefix__/g, formCount);
    $(row).html(replace_prefix);

    $(row).find('*').each(function () {
        updateElementIndex(this, prefix, formCount);
        //commented because any tag with value is always an issue
        // $(this).val('');
    });
    $(row).find('.delete-row').click(function () {
        deleteForm(this, prefix);
    });
    $('#id_' + prefix + '-TOTAL_FORMS').val(formCount + 1);
    $('#dynamic_form_table tbody').append($(row));
    return false;
}


function deleteForm(btn, prefix) {
    $(btn).parents('.dynamic-form').remove();
    var forms = $('.dynamic-form');
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i = 0, formCount = forms.length; i < formCount; i++) {
        $(forms.get(i)).find('*').each(function () {
            updateElementIndex(this, prefix, i);
        });
    }
    return false;
}
