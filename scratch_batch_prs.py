import subprocess, os

tasks = [
    {
        'repo_dir': r'C:\Users\tupyn\projects\organizations\tupynambalucas-dev\org-core\foundation',
        'repo_name': 'tupynambalucas-dev/foundation',
        'branch': 'fix/changelog-docusaurus-alignment',
        'commit_msg': 'fix(changelog): align cliff toml and changelog with foundation repository naming and docusaurus format',
        'pr_title': 'fix(changelog): align cliff toml and changelog with foundation repository naming and docusaurus format',
        'pr_body': 'Aligns git-cliff Tera template with Docusaurus PR links, updates repository references from workstation to foundation, and pins git-cliff-action to commit SHA.'
    },
    {
        'repo_dir': r'C:\Users\tupyn\projects\organizations\tupynambalucas-dev\org-core\platform',
        'repo_name': 'tupynambalucas-dev/platform',
        'branch': 'ci/deploy-release-please-workflow',
        'commit_msg': 'ci(release): deploy automated release-please workflow with ci-bot app token',
        'pr_title': 'ci(release): deploy automated release-please workflow with ci-bot app token',
        'pr_body': 'Deploys automated release-please workflow leveraging ci-bot GitHub App authentication for Manifest Mode changelog updates.'
    },
    {
        'repo_dir': r'C:\Users\tupyn\projects\organizations\tupynambalucas-dev\org-core\docs',
        'repo_name': 'tupynambalucas-dev/docs',
        'branch': 'docs/deploy-git-cliff-configuration',
        'commit_msg': 'docs(changelog): deploy declarative git-cliff configuration conforming to docusaurus format',
        'pr_title': 'docs(changelog): deploy declarative git-cliff configuration conforming to docusaurus format',
        'pr_body': 'Deploys root cliff.toml configured with Docusaurus PR links and symmetrical Keep a Changelog taxonomy.'
    },
    {
        'repo_dir': r'C:\Users\tupyn\projects\organizations\tupynambalucas-dev\org-core',
        'repo_name': 'tupynambalucas-dev/org-core',
        'branch': 'fix/changelog-docusaurus-alignment',
        'commit_msg': 'fix(changelog): align git-cliff template with docusaurus pr link standard',
        'pr_title': 'fix(changelog): align git-cliff template with docusaurus pr link standard',
        'pr_body': 'Fixes git-cliff Tera template to preserve conventional commit types and scopes while preventing duplicate PR numbers in merge commits.'
    },
    {
        'repo_dir': r'C:\Users\tupyn\projects\organizations\tupynambalucas-dev\org-core\.github',
        'repo_name': 'tupynambalucas-dev/.github',
        'branch': 'fix/changelog-docusaurus-alignment',
        'commit_msg': 'fix(changelog): align git-cliff template with docusaurus pr link standard',
        'pr_title': 'fix(changelog): align git-cliff template with docusaurus pr link standard',
        'pr_body': 'Fixes git-cliff Tera template to preserve conventional commit types and scopes while preventing duplicate PR numbers in merge commits.'
    },
    {
        'repo_dir': r'C:\Users\tupyn\projects\organizations\tupynambalucas-dev\org-core\.github-private',
        'repo_name': 'tupynambalucas-dev/.github-private',
        'branch': 'docs/initialize-changelog-and-git-cliff',
        'commit_msg': 'docs(changelog): initialize authoritative git-cliff config and keep a changelog file',
        'pr_title': 'docs(changelog): initialize authoritative git-cliff config and keep a changelog file',
        'pr_body': 'Initializes root cliff.toml and Keep a Changelog file following enterprise Docusaurus standards for .github-private.'
    },
    {
        'repo_dir': r'C:\Users\tupyn\projects\organizations\tupynambalucas-dev\org-ecosystem',
        'repo_name': 'tupynambalucas-dev/org-ecosystem',
        'branch': 'fix/changelog-docusaurus-alignment',
        'commit_msg': 'fix(changelog): align git-cliff template with docusaurus pr link standard',
        'pr_title': 'fix(changelog): align git-cliff template with docusaurus pr link standard',
        'pr_body': 'Fixes git-cliff Tera template to preserve conventional commit types and scopes while preventing duplicate PR numbers in merge commits.'
    },
    {
        'repo_dir': r'C:\Users\tupyn\projects\organizations\tupynambalucas-dev\org-ecosystem\commercial\omnichannel',
        'repo_name': 'tupynambalucas-dev/omnichannel',
        'branch': 'docs/deploy-git-cliff-configuration',
        'commit_msg': 'docs(changelog): deploy declarative git-cliff configuration conforming to docusaurus format',
        'pr_title': 'docs(changelog): deploy declarative git-cliff configuration conforming to docusaurus format',
        'pr_body': 'Deploys root cliff.toml configured with Docusaurus PR links and symmetrical Keep a Changelog taxonomy.'
    },
    {
        'repo_dir': r'C:\Users\tupyn\projects\organizations\tupynambalucas-dev\org-ecosystem\internal\tessel',
        'repo_name': 'tupynambalucas-dev/tessel',
        'branch': 'docs/deploy-git-cliff-configuration',
        'commit_msg': 'docs(changelog): deploy declarative git-cliff configuration conforming to docusaurus format',
        'pr_title': 'docs(changelog): deploy declarative git-cliff configuration conforming to docusaurus format',
        'pr_body': 'Deploys root cliff.toml configured with Docusaurus PR links and symmetrical Keep a Changelog taxonomy.'
    }
]

for t in tasks:
    r_dir = t['repo_dir']
    r_name = t['repo_name']
    branch = t['branch']
    c_msg = t['commit_msg']
    pr_t = t['pr_title']
    pr_b = t['pr_body']

    print(f'=== Processing {r_name} ===')
    try:
        # Check current branch or switch
        subprocess.run(['git', 'checkout', '-b', branch], cwd=r_dir, check=True)
        subprocess.run(['git', 'add', '.'], cwd=r_dir, check=True)
        subprocess.run(['git', 'commit', '-S', '-m', c_msg], cwd=r_dir, check=True)
        subprocess.run(['git', 'push', '-u', 'origin', branch], cwd=r_dir, check=True)
        pr_out = subprocess.check_output(
            ['gh', 'pr', 'create', '--repo', r_name, '--title', pr_t, '--body', pr_b],
            cwd=r_dir, text=True
        )
        print(f'Created PR: {pr_out.strip()}')
    except Exception as e:
        print(f'Error on {r_name}: {e}')
