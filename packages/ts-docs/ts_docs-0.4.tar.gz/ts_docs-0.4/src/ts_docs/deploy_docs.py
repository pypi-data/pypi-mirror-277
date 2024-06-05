# See the License for the specific language governing permissions and
# limitations under the License.
#
import argparse
import glob
import os
import os.path
import re
import stat
import subprocess
import tarfile

import packaging.version


def env(variable, default=None):
    """ Shortcut to return the expanded version of an environment variable """
    return os.path.expandvars(os.environ.get(variable, default) if default else os.environ[variable])


from .sanitize_version import sanitize_version  # noqa


def main():
    parser = argparse.ArgumentParser(description='deploy_docs.py: Deploy timesintelli docs', prog='deploy_docs.py')
    parser.add_argument('--ver', '-v', type=str, default='latest')
    parser.add_argument('--docs-path', '-p', type=str, default='')
    args = parser.parse_args()

    os.environ['DOCS_BUILD_DIR'] = "{}/docs/_build".format(args.docs_path)
    os.environ['DOCS_DEPLOY_URL_BASE'] = "file://{}/docs".format(args.docs_path)
    os.environ['DOCS_DEPLOY_PATH'] = "{}/docs/deploy".format(args.docs_path)
    os.environ['TYPE'] = "preview"
    os.environ['DEPLOY_STABLE'] = ""

    version = sanitize_version(args.ver)
    print('CI Version: {}'.format(args.ver))
    print('Deployment version: {}'.format(version))

    if not version:
        raise RuntimeError('A version is needed to deploy')

    build_dir = env('DOCS_BUILD_DIR')  # top-level local build dir, where docs have already been built

    if not build_dir:
        raise RuntimeError('Valid DOCS_BUILD_DIR is needed to deploy')

    url_base = env('DOCS_DEPLOY_URL_BASE')  # base for HTTP URLs, used to print the URL to the log after deploying

    docs_path = env('DOCS_DEPLOY_PATH')  # filesystem path 

    if not docs_path:
        raise RuntimeError('Valid DOCS_DEPLOY_PATH is needed to deploy')

    print('DOCS_DEPLOY_PATH {}'.format(docs_server, docs_path))

    tarball_path, version_urls = build_doc_tarball(version, build_dir)

    deploy(version, tarball_path, docs_path)

    print('Docs URLs:')
    doc_deploy_type = os.getenv('TYPE')
    for vurl in version_urls:
        language, _, target = vurl.split('/')
        tag = '{}_{}'.format(language, target)
        url = '{}/{}/index.html'.format(url_base, vurl)  # (index.html needed for the preview server)
        url = re.sub(r'([^:])//', r'\1/', url)  # get rid of any // that isn't in the https:// part
        print('[document {}][{}] {}'.format(doc_deploy_type, tag, url))

    # note: it would be neater to use symlinks for stable, but because of the directory order
    # (language first) it's kind of a pain to do on a remote server, so we just repeat the
    # process but call the version 'stable' this time


def deploy(version, tarball_path, docs_path):
    subprocess.run(['mkdir', '-p', docs_path], check=True)
    tarball_name = os.path.basename(tarball_path)

    subprocess.run(['cp', tarball_path, docs_path], check=True)

    cmds = "cd {}; rm -rf ./*/{}; tar -zxvf {}; rm {};".format(docs_path, version, tarball_name, tarball_name)
    subprocess.run(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def build_doc_tarball(version, build_dir):
    """ Make a tar.gz archive of the docs, in the directory structure used to deploy as
        the given version """
    version_paths = []
    tarball_path = '{}/{}.tar.gz'.format(build_dir, version)

    # find all the 'html/' directories under build_dir
    html_dirs = glob.glob('{}/**/html/'.format(build_dir), recursive=True)
    print('Found %d html directories' % len(html_dirs))

    pdfs = glob.glob('{}/**/latex/build/*.pdf'.format(build_dir), recursive=True)
    print('Found %d PDFs in latex directories' % len(pdfs))

    # todo: add symlink for stable and latest and adds them to PDF blob

    def not_sources_dir(ti):
        """ Filter the _sources directories out of the tarballs """
        if ti.name.endswith('/_sources'):
            return None

        ti.mode |= stat.S_IWGRP  # make everything group-writeable
        return ti

    try:
        os.remove(tarball_path)
    except OSError:
        pass

    with tarfile.open(tarball_path, 'w:gz') as tarball:
        for html_dir in html_dirs:
            # html_dir has the form '<ignored>/<language>/<target>/html/'
            target_dirname = os.path.dirname(os.path.dirname(html_dir))
            target = os.path.basename(target_dirname)
            language = os.path.basename(os.path.dirname(target_dirname))

            # when deploying, we want the top-level directory layout 'language/version/target'
            archive_path = '{}/{}/{}'.format(language, version, target)
            print("Archiving '{}' as '{}'...".format(html_dir, archive_path))
            tarball.add(html_dir, archive_path, filter=not_sources_dir)
            version_paths.append(archive_path)

        for pdf_path in pdfs:
            # pdf_path has the form '<ignored>/<language>/<target>/latex/build'
            latex_dirname = os.path.dirname(pdf_path)
            pdf_filename = os.path.basename(pdf_path)
            target_dirname = os.path.dirname(os.path.dirname(latex_dirname))
            target = os.path.basename(target_dirname)
            language = os.path.basename(os.path.dirname(target_dirname))

            # when deploying, we want the layout 'language/version/target/pdf'
            archive_path = '{}/{}/{}/{}'.format(language, version, target, pdf_filename)
            print("Archiving '{}' as '{}'...".format(pdf_path, archive_path))
            tarball.add(pdf_path, archive_path)

    # todo: for symlink in symlinks:

    return (os.path.abspath(tarball_path), version_paths)
    

if __name__ == '__main__':
    main()
