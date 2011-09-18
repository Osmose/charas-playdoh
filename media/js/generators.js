(function() {

var GENERATOR_SLUG = $('#generator_app').data('generator');
var PART_API = '/generators/api/v1/part';
var RESOURCE_API = '/generators/api/v1/resource';

function Generator() {
    this.canvas = document.createElement('canvas');
    this.width = this.canvas.width = 72;
    this.height = this.canvas.height = 128;

    this.ctx = this.canvas.getContext('2d');
    this.layers = {};
    this.drawLayers = [];
    this.drawLayerComparitor = this.drawLayerComparitor();

    this.parts = {};
    this.resources = {};

    this.previewContainer = $('#preview-container');

    this.bindEvents();
    this.loadParts();
    this.redraw();
    this.refreshPreview();
}
var p = Generator.prototype;

p.loadParts = function() {
    var self = this;
    $.ajax({
        url: PART_API,
        data: {generator__slug: GENERATOR_SLUG},
        success: function(data) {
            $.each(data.objects, function(k, part) {
                self.layers[part.slug] = {
                    order: part.order,
                    img: null
                };
                self.drawLayers.push(part.slug);
                self.parts[part.id] = part;
            });
            self.drawLayers.sort(self.drawLayerComparitor);

            $('#parts_view').html(ich.parts_tabs({parts: data.objects})).tabs();
            self.loadResources();
        }
    });
};

p.loadResources = function() {
    var self = this;
    $.each(self.parts, function(k, part) {
        $.ajax({
            url: RESOURCE_API,
            data: {part__slug: part.slug},
            success: function(data) {
                $.each(data.objects, function(i, resource) {
                    self.resources[resource.id] = resource;
                });

                $('#parts-' + part.slug)
                    .html(ich.resources_view({part_slug: part.slug,
                                              resources: data.objects}));
            }
        });
    });
};

p.chooseResource = function(el) {
    var self = this;
    var $el = $(el);
    var id = $el.data('resource-id');
    var part_slug = $el.data('part-slug');

    var img = new Image();
    img.onload = function() {
        self.redraw();
        self.refreshPreview();
    };
    img.src = this.resources[id].resource;
    this.layers[part_slug].img = img;
};

p.redraw = function() {
    var self = this;
    self.ctx.clearRect(0, 0, self.width, self.height);
    $.each(this.drawLayers, function(k, part_slug) {
        if (self.layers[part_slug].img != null) {
            self.ctx.drawImage(self.layers[part_slug].img, 0, 0);
        }
    });
};

p.refreshPreview = function() {
    var png = Canvas2Image.saveAsPNG(this.canvas, true);
    this.previewContainer.html(png);
};

p.bindEvents = function() {
    var self = this;
    $('.resource').live('click', function() {
        self.chooseResource(this);
    });

    // Download Button
    $('#download').click(function() {
        Canvas2Image.saveAsPNG(self.canvas);
    });
};

p.drawLayerComparitor = function() {
    var self = this;
    return function(a, b) {
        var av = self.layers[a].order,
            bv = self.layers[b].order;
        return av - bv;
    };
};

$(function() {
    window.CharasGenerator = new Generator();
});

})();
