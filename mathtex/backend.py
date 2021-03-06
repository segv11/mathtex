class MathtexBackend(object):
    """
    The base class for all Mathtex backends.
    """

    def __init__(self):
        self._options = {}

    def set_canvas_size(self, w, h, d, dpi):
        self.width = w
        self.height = h
        self.depth = d
        self.dpi = dpi

    def render(self, glyphs, rects):
        """
        Renders the generated list of glyphs and rectangles.
        """
        raise NotImplementedError()

    def get_results(self):
        raise NotImplementedError()

    def save(self, filename, format):
        """
        Saves the outputed generated by the backend. *filename* is the name of
        the generated output while *format* is the format to save it in.

        :math:`get_formats` can be used to query the formats supported by this
        backend.
        """
        raise NotImplementedError()

    def get_formats(self):
        """
        Returns a list of output formats supported by this backend.
        """
        return []

    def get_options(self):
        """
        Returns a dictionary containing 'option name' : value for each
        configuration option supported by this backend.
        """
        return self._options

    def set_options(self, newoptions):
        self._options.update(newoptions)

    options = property(get_options, set_options)

    def set_option(self, option, value):
        self._options[option] = value
