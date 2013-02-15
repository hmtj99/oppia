# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Controllers for Oppia exploration statistics page."""

__author__ = 'sll@google.com (Sean Lip)'

from controllers.base import BaseHandler, require_editor
import feconf
import utils


class StatsHandler(BaseHandler):
    """Handles display of the statistics page for explorations."""

    @require_editor
    def get(self, unused_user, exploration):  # pylint: disable-msg=C6409
        """Displays the statistics page for the given exploration."""

        self.values.update({
            'js': utils.GetJsFilesWithBase(['stats'])
        })
        self.response.out.write(feconf.JINJA_ENV.get_template(
            'stats.html').render(self.values))
