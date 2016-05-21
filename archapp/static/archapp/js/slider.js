(function(jQuery) {
    $(document).ready(function($){
        var d = $('#id_dating');

        if( d.length )
        {
            var l = $("<span id = 'slider_label'>aewoeirn908</span>")
            var z = $("<div id = 'slider'></div>");
            var x = function(e, ui) {
                var r1 = d.find('option').eq(ui.values[0] - 1);
                var r2 = d.find('option').eq(ui.values[1] - 1);
                $('#id_datingfrom').val(r1[0].value);
                $('#id_datingto').val(r2[0].value);
                l.html(r1.text() + ' - ' + r2.text()); }
            var s = z.slider({
                min: 1,
                max: 8,
                range: true,
                values: [d[0].selectedIndex, d[0].selectedIndex ],
                slide: x });
            $('#id_undefined').click(function(){
                if ($(this).is(':checked'))
                {
                    z.slider('option', 'disabled', true);
                    l.html('---');
                }
                else
                {
                    z.slider('option', 'disabled', false);
                    z.trigger('slidechange');
                    x(null, z.slider("instance").options);
                }
            });

            z.addClass('col-md-2 col-md-offset-6');
            d.hide();
            d.after(l);
            l.after(z);

            z.slider('values', [1, 3]);
            x(null, z.slider("instance").options);
        }

    });
})()
