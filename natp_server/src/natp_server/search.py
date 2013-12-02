from django.shortcuts import render
from django.http import HttpResponse
from models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required





@login_required
def search_probe(request):
    pro = Probe.objects.all()
    if 'pbname' in request.POST:
        pbname = request.POST['pbname']
    else:
        pbname = ""
    if 'prov' in request.POST:
        province = request.POST['prov']
    else:
        province = ""
    if 'gps' in request.POST:
        gps = request.POST['gps']
    else:
        gps = ""
    if not pbname and not province and not gps:
        return render_to_response('search_probe.html',context_instance=RequestContext(request))
    if  pbname:
        pro = pro.filter(probe_name=pbname)
    if province:
        pro = pro.filter(province=province)
    if gps:
        pro = pro.filter(gps=gps)
       
    return render_to_response('search_probe_result.html',{'pro':pro},context_instance=RequestContext(request))


@login_required
def search_position(request):
    probes = Probe.objects.all()
    if 'icao' in request.POST:
        icao = request.POST['icao']
    else:
        icao = ""
    if 'seen' in request.POST:
        seen = request.POST['seen']
    else:
        seen = ""
    if 'alt' in request.POST:
        alt = request.POST['alt']
    else:
        alt = ""
    if 'lat' in request.POST:
        lat = request.POST['lat']
    else:
        lat = ""
    if 'lon' in request.POST:
        lon = request.POST['lon']
    else:
        lon = ""
    if 'probe' in request.POST:
        pr = request.POST['probe']
        if pr:
            probe = Probe.objects.get(probe_name=pr)
        else:
            probe = ""
    else:
        probe = ""
    if not icao and not seen and not alt and not lat and not lon and not probe:
        return render_to_response('search_position.html',{'probes':probes},context_instance=RequestContext(request))    
    po = Position.objects.all()
    if icao:
        po = po.filter(icao=icao)
    if seen:
        po = po.filter(seen=seen)
    if alt:
        po = po.filter(alt=alt)
    if lat:
        po = po.filter(lat=lat)
    if  lon:
        po = po.filter(lon=lon)
    if probe:
        po = po.filter(probe=probe)
    
    return render_to_response('search_position_result.html',{'po':po,'probes':probes},context_instance=RequestContext(request))

@login_required
def search_vector(request):
    probes = Probe.objects.all()
    ve = Vector.objects.all()
    if 'icao' in request.POST:
        icao = request.POST['icao']
    else:
        icao = ""
    if 'seen' in request.POST:
        seen = request.POST['seen']
    else:
        seen = ""
    if 'speed' in request.POST:
        speed = request.POST['speed']
    else:
        speed = ""
    if 'heading' in request.POST:
        heading = request.POST['heading']
    else:
        heading = ""
    if 'vertical' in request.POST:
        vertical = request.POST['vertical']
    else:
        vertical = ""
    if 'probe' in request.POST:
        pr = request.POST['probe']
        if pr:
            probe = Probe.objects.get(probe_name=pr)
        else:
            probe = ""
    else:
        probe = ""
    if not icao and not seen and not speed and not heading and not vertical and not probe:
       return render_to_response('search_vector.html',{'probes':probes},context_instance=RequestContext(request))
    if icao:
        ve = ve.filter(icao=icao)
    if seen:
        ve = ve.filter(seen=seen)
    if speed:
        ve = ve.filter(speed=speed)
    if heading:
        ve = ve.filter(heading=heading)
    if vertical:
        ve = ve.filter(vertical=vertical)
    if probe:
        ve = ve.filter(probe=probe)
    return render_to_response('search_vector_result.html',{'ve':ve},context_instance=RequestContext(request))
    

@login_required
def search_ident(request):
    idt = Ident.objects.all()
    probes = Probe.objects.all()
    if 'icao' in request.POST:
        icao = request.POST['icao']
    else:
        icao = ""
    if 'ident' in request.POST:
        ident = request.POST['ident']
    else:
        ident = ""
    if 'probe' in request.POST:
        pr = request.POST['probe']
        if pr:
            probe = Probe.objects.get(probe_name=pr)
        else:
            probe = ""
    else:
        probe=""
    if not icao and not ident and not probe:
       return render_to_response('search_ident.html',{'probes':probes},context_instance=RequestContext(request))
    if icao:
        idt = idt.filter(icao=icao)
    if ident:
        idt = idt.filter(ident=ident)
    if probe:
        idt = idt.filter(probe=probe)
    return render_to_response('search_ident_result.html',{'idt':idt},context_instance=RequestContext(request))
