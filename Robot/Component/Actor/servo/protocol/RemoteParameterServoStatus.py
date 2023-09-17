from RoboControl.Com.Remote.Parameter.RemoteParameter import RemoteParameter

FLAG_IS_ON = 0
FLAG_IS_ACTIVE = 1
FLAG_REVERSE = 2
FLAG_IS_AT_MIN = 3
FLAG_IS_AT_MAX = 4
FLAG_IS_STALLING = 5


class RemoteParameterServoStatus(RemoteParameter):

    def __init__(self, name, description):
        super().__init__(name, description, 2)

        self._reverse = False
        self._on = False
        self._active = False
        self._is_at_min = False
        self._is_at_max = False
        self._stalling = False

    def set_reverse(self, status):
        self._reverse = status

    def is_reverse(self):
        return self._reverse

    def set_on(self, status):
        self._on = status

    def is_on(self):
        return self._on

    def set_active(self, status):
        self._active = status

    def is_active(self):
        return self._active

    def set_at_min(self, status):
        self._is_at_min = status

    def is_at_min(self):
        return self._is_at_min

    def set_at_max(self, status):
        self._is_at_max = status

    def is_at_max(self):
        return self._is_at_max

    def set_stalling(self, status):
        self._stalling = status

    def is_stalling(self):
        return self._stalling

    def parse_from_buffer(self, data_buffer, index):

        flags = data_buffer[index]

        if (flags & (1 << FLAG_REVERSE)) > 0:
            self._reverse = True
        else:
            self._reverse = False

        if (flags & (1 << FLAG_IS_ON)) > 0:
            self._on = True
        else:
            self._on = False

        if (flags & (1 << FLAG_IS_ACTIVE)) > 0:
            self._active = True
        else:
            self._active = False

        if (flags & (1 << FLAG_IS_AT_MIN)) > 0:
            self._is_at_min = True
        else:
            self._is_at_min = False

        if (flags & (1 << FLAG_IS_AT_MAX)) > 0:
            self._is_at_max = True
        else:
            self._is_at_max = False

        if (flags & (1 << FLAG_IS_STALLING)) > 0:
            self._stalling = True

        else:
            self._stalling = False

        return self._byte_size

    def get_as_buffer(self):

        flags = 0

        if self._reverse:
            flags |= (1 << FLAG_REVERSE)

        if self._on:
            flags |= (1 << FLAG_IS_ON)

        if self._active:
            flags |= (1 << FLAG_IS_ACTIVE)

        if self._is_at_min:
            flags |= (1 << FLAG_IS_AT_MIN)

        if self._is_at_max:
            flags |= (1 << FLAG_IS_AT_MAX)

        if self._stalling:
            flags |= (1 << FLAG_IS_STALLING)

        buffer = bytearray(self._byte_size)
        buffer[0] = flags

        return buffer


"""


@Override
public String getAsString(boolean description)
{
    String returnString ="";
    
    if (description)
    {
        returnString+= RemoteParameterServoStatus.name+" ";
        
        returnString+= "on="+ this.on;
        returnString+= ", reverse="+this.reverse;
        returnString+= ", active="+this.active;
        returnString+= ", isAtMin="+this.isAtMin;
        returnString+= ", isAtMax="+this.isAtMax;
        returnString+= ", stalling="+this.stalling;
        
    }
    else
    {
        returnString+= this.on+", ";
        returnString+= this.reverse;
        
    }
        
    return(returnString);
}


}
"""
