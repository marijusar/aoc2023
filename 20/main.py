import json
import math

f = open("./input.txt")
lines = [x.strip() for x in f.readlines()]

pulse_types = {
    "H" : "H",
    "L" : "L"
}


class FlipFlopModule :
    state = False 
    pending_pulse = None

    def receive_pulse(self,pulse,sender) :
        if pulse == pulse_types["H"] :
            self.pending_pulse = None
       
        if pulse == pulse_types["L"] :
            temp_state = self.state
            self.state = not self.state
            if temp_state  == False :
                self.pending_pulse =  pulse_types["H"]
            else :
                self.pending_pulse =  pulse_types["L"]

    def send_pulse(self, target):
        return self.pending_pulse

class ConjunctionModule :
    def __init__(self) :
        self.mem = {}
    def receive_pulse(self, pulse, sender):
        self.mem[sender] = pulse

    def send_pulse(self, target) :
        v = list(self.mem.values())
        l = [x for x in v if x == pulse_types["L"]]
        if len(l) > 0 :
            return pulse_types["H"]

        return pulse_types["L"]
    def subscribe(self, m) :
        self.mem[m] = "L"

class BroadcastModule :
    pending_pulse = None

    def receive_pulse(self, pulse, sender) :
        self.pending_pulse = pulse

    def send_pulse(self, target) :
        return self.pending_pulse

module_map = {
    "%" : FlipFlopModule,
    "&" : ConjunctionModule,
    "b" : BroadcastModule
}

modules = {}
conj = []
for i in lines :
    module, receivers = i.split("->")

    m_t = module[0:1].strip()
    m_n = module[1:].strip()
    r_a = [x.strip() for x in receivers.split(",")]

    if m_t == "&" :
        conj.append(m_n)

    m = module_map[m_t]()

    mod = {
        "m" : m,
        "r" : r_a
    }
    modules[m_n] = mod

for i in conj :
    for k in modules :
        if i in modules[k]["r"] :
            modules[i]["m"].subscribe(k)

    
def serialize_modules(m) : 
    acc= []
    for k in m :
        s = m[k]["m"].to_json()
        acc.append(s)
    i = json.dumps(acc)
    h = sha1(i.encode('utf-8')).hexdigest()
    return h

track = ["ch", "sv", "th", "gh"]
tracks = {}

def send_signal(signal, iteration) :
    s = [signal]
    l = 1
    h = 0

    while len(s) > 0 :
        s_0 = s.pop(0)
        reciever, pulse, sender = s_0 
        if reciever not in modules :
            continue
        modules[reciever]["m"].receive_pulse(pulse, sender)

        for i in modules[reciever]["r"] :
            pulse = modules[reciever]["m"].send_pulse(i)
            if not pulse :
                continue
            if pulse == "H" :
                h += 1
            if pulse == "L" :
                l += 1
            if i in track and pulse == "L" :
                if i not in tracks :
                    tracks[i] = [iteration]
                else :
                    tracks[i].append(iteration) 



            s.append((i, pulse, reciever))

    return l, h

l = range(10000)
signals = [send_signal(("roadcaster", "L", "btn"), idx + 1) for idx, x in enumerate(l)]

print(tracks)

l_s= sum([x[0] for x in signals])
h_s = sum([x[1] for x in signals])

part_one = l_s * h_s


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcms() :
    return lcm(lcm(lcm(tracks['ch'][0], tracks['gh'][0]), tracks['sv'][0]), tracks['th'][0])

part_two = lcms()

print(part_two)
