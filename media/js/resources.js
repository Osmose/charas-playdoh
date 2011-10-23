(function() {

var RESOURCE_API = '/resources/api/v1/resource';

var app = $('#resources-app'),
    app_body = $('#app-body'),
    app_heading = $('#app-heading'),
    app_categories = $('#categories'),

    gamemakers = app.data('gamemakers'),
    category_map = {},
    gamemaker_map = {},

    Resource = new Manager(RESOURCE_API);

// Populate slug-to-obj maps
for (var k = 0; k < gamemakers.length; k++) {
    var maker = gamemakers[k];
    gamemaker_map[maker['slug']] = maker;
    for (var m = 0; m < maker['categories'].length; m++) {
        var category = maker['categories'][m];
        category_map[category['slug']] = category;
    }
}

// Enable route logging
crossroads.routed.add(console.log, console);

// Show a list of recent CR uploads
crossroads.addRoute('recent', function() {
    Resource.order_by('created').eval().done(function(resources) {
        app_heading.text('Recent Resources');
        app_body.html(ich.resource_grid({
            resources: resources
        }));
    });
});

// Show resources in a category
crossroads.addRoute('category/{slug}', function(slug) {
    var category = getattr(category_map, slug);
    if (category !== null) {
        var maker = gamemaker_map[category['maker']];
        var filters = {category__slug__exact: slug, order_by: 'created'};

        Resource.filter(filters).eval().done(function(resources) {
            app_heading.text(maker['name'] + ': ' + category['name']);
            app_body.html(ich.resource_grid({
                resources: resources
            }));
        });
    }
});

// Show details about a resource
crossroads.addRoute('resource/{id}', function(id) {
    Resource.get({id: id}).done(function(resource) {
        app_heading.text(resource['name']);
        app_body.html(ich.resource_detail({
            resource: resource,
            details: [
                ['Title:', resource['name']],
                ['Author:', resource['author']],
                ['Uploaded:', (new Date(resource['created'])).toDateString()],
                ['Description:', resource['description']]
            ]
        }));
    }).fail(function() {
        app_heading.text('Failure');
    });
});

$(function() {
    // Generate category listing
    app_categories.html(ich.category_tree({
        gamemakers: gamemakers
    }));

    // Hasher handles history
    hasher.initialized.add(crossroads.parse, crossroads); //parse initial hash
    hasher.changed.add(crossroads.parse, crossroads); //parse hash changes
    hasher.init(); //start listening for history change

    // Init app with recent route
    var curHash = hasher.getHash();
    if (curHash == '') {
        hasher.setHash('recent');
    }
});

})();
