// Returns an attribute on an object, or a default value
// if the attribute isn't on the object.
function getattr(obj, attr, def) {
    if (def === undefined) def = null;

    if (!(attr in obj)) {
        return def;
    } else {
        return obj[attr];
    }
}
