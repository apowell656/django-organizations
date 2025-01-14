# -*- coding: utf-8 -*-

# Copyright (c) 2012-2019, Ben Lopatin and contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.  Redistributions in binary
# form must reproduce the above copyright notice, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided with
# the distribution
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from organizations.views import default as views


# app_name = "organizations"

urlpatterns = [
    url(
        r"^$",
        view=login_required(views.OrganizationList.as_view()),
        name="organization_list",
    ),
    url(
        r"^add/$",
        view=login_required(views.OrganizationCreate.as_view()),
        name="organization_add",
    ),
    url(
        r"^(?P<organization_pk>[0-9a-f-]+)/",
        include(
            [
                url(
                    r"^$",
                    view=login_required(views.OrganizationDetail.as_view()),
                    name="organization_detail",
                ),
                url(
                    r"^edit/$",
                    view=login_required(views.OrganizationUpdate.as_view()),
                    name="organization_edit",
                ),
                url(
                    r"^delete/$",
                    view=login_required(views.OrganizationDelete.as_view()),
                    name="organization_delete",
                ),
                url(
                    r"^people/",
                    include(
                        [
                            url(
                                r"^$",
                                view=login_required(
                                    views.OrganizationUserList.as_view()
                                ),
                                name="organization_user_list",
                            ),
                            url(
                                r"^add/$",
                                view=login_required(
                                    views.OrganizationUserCreate.as_view()
                                ),
                                name="organization_user_add",
                            ),
                            url(
                                r"^(?P<user_pk>[0-9a-f-]+)/remind/$",
                                view=login_required(
                                    views.OrganizationUserRemind.as_view()
                                ),
                                name="organization_user_remind",
                            ),
                            url(
                                r"^(?P<user_pk>[0-9a-f-]+)/$",
                                view=login_required(
                                    views.OrganizationUserDetail.as_view()
                                ),
                                name="organization_user_detail",
                            ),
                            url(
                                r"^(?P<user_pk>[0-9a-f-]+)/edit/$",
                                view=login_required(
                                    views.OrganizationUserUpdate.as_view()
                                ),
                                name="organization_user_edit",
                            ),
                            url(
                                r"^(?P<user_pk>[0-9a-f-]+)/delete/$",
                                view=login_required(
                                    views.OrganizationUserDelete.as_view()
                                ),
                                name="organization_user_delete",
                            ),
                        ]
                    ),
                ),
            ]
        ),
    ),
]
