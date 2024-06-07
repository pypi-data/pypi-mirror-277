"""
simple wall-clock based recording timer
"""
import time
from dataclasses import dataclass
import pandas as pd

class Timer():
    """
    simple wall-clock based recording timer
    
    
    USAGE
    
    .. code-block:: python
    
        timer = Timer()
        timer.record("event1")
        timer.record("event2")
        result = timer.end() 
    """
    def __init__(self):
        self.start_time = time.time()
        self.records = []
        
    def record(self, event=None, data=None):
        """
        records an event
        
        :event:     the event to record (default: ``event #x``)
        :data:      additional data to record (default: None)
        """
        data = data or dict()
        assert isinstance(data, dict), f"data must be a dict {data}"
        event = event or f"event #{len(self.records)+1}"
        self.records.append((event, time.time()-self.start_time, data))
        return self.result
        
    def end(self, event=None, data=None):
        """calls record() with default event ``end``"""
        if event is None: event = "end"
        return self.record(event, data)
    
    @property
    def result(self):
        """returns the result of the timer as ``TimerRecord``"""
        return self.TimerRecord(self.start_time, self.records)
    
    def __call__(self):
        """returns the result of the timer as ``TimerRecord``"""
        return self.result
    
    @dataclass    
    class TimerRecord():
        """
        simple class to hold a timer record
        """
        start_time: float
        records: list
        
        def as_df(self, incl_data=False):
            """
            converts this record to a ``DataFrame``
            
            :incl_data:     if ``True``, includes the data in the DataFrame (default: False)
            """
            records = (r[:2] for r in self.records)
            df = pd.DataFrame(records, columns=["event", "time"])
            df["marginal"] = df['time'].diff().fillna(df['time'].iloc[0])
            if incl_data:
                df = pd.concat([df, self.data(as_df=True)], axis=1)
            return df
        
        def data(self, as_df=False):
            """
            returns the data from the records, by default as ``list``
            
            :as_df:     if ``True``, returns the data as a ``DataFrame`` (default: False)
            """
            result = [r[2] for r in self.records]
            return result if not as_df else pd.DataFrame(result)
        
        def total(self):
            """
            returns the total time
            """
            return self.records[-1][1]
        
        def __len__(self):
            return len(self.records)
        
        def __float__(self):
            return float(self.total())
        
        def __int__(self):
            return int(float(self))