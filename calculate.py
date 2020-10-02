import users, visits, os, orders, customers, datetime, events

def seek_slowest():
    biglist = dict()
    orders_all = orders.listAll()

    for o in orders_all:
        e_by_o = events.list(o[0])
        eventsl = dict()
        events_seen = dict()
        # loop events linked to this order_id
        # add event descr. to dict key and timestamp to value - if events status is pending
        # then add difference of timestamps if met the same description with event status not pending
        for e in e_by_o:
            # change the datetime to int
            dt = e[3]
            seq = int(dt.strftime("%Y%m%d%H%M%S"))
            if e[5] in eventsl and e[4] == 0:
                eventsl[e[5]] = abs(eventsl.get(e[5])-seq)
                events_seen[e[5]] = events_seen[e[5]] + 1
            elif e[5] not in eventsl and e[4] == 1:
                eventsl[e[5]] = seq
                events_seen[e[5]] = 1
            elif e[5] not in eventsl and e[4] == 0:
                eventsl[e[5]] = seq
                events_seen[e[5]] = 1
            else:
                events_seen[e[5]] = events_seen[e[5]] + 1

        # to ensure there are only differences calculated when seen two events for one description:
        for event in events_seen:
            if events_seen.get(event) < 2 or events_seen.get(event) > 2:
                del eventsl[event]
        
        # adding every found event to biglist and calculate mean when adding
        for desc, time in eventsl.items():
            if desc not in biglist:
                biglist[desc] = time
            else:
                old = 0
                old = biglist[desc]
                biglist[desc] =  (time + old) / 2

    sort_durations = sorted(biglist.items(), key=lambda x: x[1], reverse=True)

    return sort_durations
