class Config:
    """
    Config file for the series opening recognizer.

    Attributes:
    RATE: int
        Audio sample rate.
    MIN_SEGMENT_LENGTH_SEC: int
        Minimum length of the intro in seconds.
    MIN_SEGMENT_LENGTH_BEATS: int
        Minimum length of the intro in beats.
    PRECISION_SECS: float
        Precision of the correlation in seconds.
    PRECISION_BEATS: int
        Precision of the correlation in beats.
    SERIES_WINDOW: int
        Number of sequential audio samples to be matched with each other.
        E.g. 5 means that the first sample will be matched with the next 5 samples.
    OFFSET_SEARCHER__SEQUENTIAL_SECS: int
        Number of sequential 'non-intro' seconds that signal the end of the intro.
        Intro is considered to be over if the number of sequential 'non-intro' beats is greater than this value.
    OFFSET_SEARCHER__SEQUENTIAL_INTERVALS: int
        Number of sequential 'non-intro' beats that signal the end of the intro.
    SAVE_INTERMEDIATE_RESULTS: bool
        Save the correlation results to 'correlations' and 'offsets' folders.
        Make sure to create the folder before running the app.
    """

    def __init__(self,
                 rate: int = 44100,
                 min_segment_length_sec: int = 30,
                 precision_secs: float = .5,
                 series_window: int = 5,
                 offset_searcher__sequential_secs: int = 30,
                 save_intermediate_results: bool = False):
        """
        Initialize the configuration
        :param rate: Audio sample rate.
        :param min_segment_length_sec: Minimum length of the intro in seconds.
        :param precision_secs: Precision of the correlation in seconds.
        :param series_window: Number of sequential audio samples to be matched with each other.
        :param offset_searcher__sequential_secs: Number of sequential 'non-intro' seconds that signal the end of the intro.
        :param save_intermediate_results: Save the correlation results.
        """
        self.RATE = rate

        self.MIN_SEGMENT_LENGTH_SEC = min_segment_length_sec
        self.MIN_SEGMENT_LENGTH_BEATS = int(min_segment_length_sec * rate)

        self.PRECISION_SECS = precision_secs
        self.PRECISION_BEATS = int(precision_secs * rate)

        self.SERIES_WINDOW = series_window

        self.OFFSET_SEARCHER__SEQUENTIAL_SECS = offset_searcher__sequential_secs
        self.OFFSET_SEARCHER__SEQUENTIAL_INTERVALS = int(offset_searcher__sequential_secs / precision_secs)

        self.SAVE_INTERMEDIATE_RESULTS = save_intermediate_results
