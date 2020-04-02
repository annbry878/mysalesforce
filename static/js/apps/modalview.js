$(".read-data").each(function() {
  $(this).modalForm({
    formURL: $(this).data('id')
  });
});
