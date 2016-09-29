# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from uploader.myapp.models import Document
from uploader.myapp.forms import DocumentForm


def list(request):
    # upload file
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # redirect to list
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # empty form

    # load documents
    documents = Document.objects.all()

    # render list page and form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )
