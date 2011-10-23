function Manager(path) {
    this.path = path;
}

Manager.prototype = {
    all: function() {
        return new Queryset(this.path);
    },
    filter: function(args) {
        return new Queryset(this.path, args);
    },
    limit: function(limit) {
        return new Queryset(this.path, {limit: limit});
    },
    order_by: function(order) {
        return new Queryset(this.path, {order_by: order});
    },
    get: function(args) {
        return new Queryset(this.path).get(args);
    },
    each: function(func) {
        return new Queryset(this.path).each(func);
    }
};

function Queryset(path, args) {
    this.path = path;
    this.args = args || {};
    this.result = $.Deferred();
}

Queryset.prototype = {
    filter: function(args) {
        return this._extend(args);
    },
    limit: function(limit) {
        return this._extend({limit: limit});
    },
    order_by: function(order) {
        return this._extend({order_by: order_by});
    },
    eval: function() {
        return this._result();
    },
    get: function(args) {
        var def = $.Deferred(),
            queryset = this;

        // If possible, limit on the server to save resources
        if (!this.result.isResolved()) {
            var new_args = $.extend({}, this.args, args);
            queryset = this._extend(new_args);
        }

        queryset._result().done(function(set) {
            if (set.length > 0) {
                def.resolve(set[0]);
            } else {
                def.reject();
            }
        }).fail(def.reject);

        return def;
    },
    each: function(func) {
        var def = $.Deferred();

        this._result().done(function(set) {
            for (var k = 0; k < set.length; k++) {
                func(set[k], k);
            }

            def.resolve(set);
        }).fail(def.reject);

        return def;
    },
    _extend: function(args) {
        var q = new Queryset(this.path, this.args);
        $.extend(q.args, args);
        return q;
    },
    _result: function() {
        if (!this.result.isResolved()) {
            this._execute();
        }

        return this.result;
    },
    _execute: function() {
        var self = this;
        $.ajax({
            url: this.path,
            data: this.args
        }).done(function(data) {
            self.result.resolve(data.objects);
        });
    }
};
