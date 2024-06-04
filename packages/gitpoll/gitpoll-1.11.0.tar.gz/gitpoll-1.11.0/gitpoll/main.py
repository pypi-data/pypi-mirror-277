#!/usr/bin/env python3

import os
import os.path as op
import time
import sys
from pyshared import Call
from argparse import ArgumentParser, Namespace
from .shell import CmdExec
from .args import parse_args
from .git import GitCmds
from .log import logger


def _log_exit(msg: str, code: int, logfunc: Call):
    """logs using the provided function and exits with the provided code."""
    logfunc(msg)
    sys.exit(code)


def _mainloop(pargs: Namespace):
    try:
        gitcmds = GitCmds(pargs.repo_path)
        if gitcmds.changed or pargs.force:
            logger.debug("Repo Change" if gitcmds.changed else "Force Exec")
            if gitcmds.changed:
                logger.info(
                    "Local: {} | Remote: {}".format(
                        gitcmds.local.output, gitcmds.remote.output
                    )
                )

            if pargs.pre_action:
                logger.debug("Pre-action: {}".format(pargs.pre_action))
                pre_cmd = CmdExec(pargs.pre_action)
                logger.info(str(pre_cmd))

            if not pargs.no_pull:
                logger.info("Pulling changes from the repository.")
                pull_cmd = CmdExec("git pull")
                logger.info(str(pull_cmd))

            if pargs.post_action:
                logger.debug("Post-action: {}".format(pargs.post_action))
                post_cmd = CmdExec(pargs.post_action)
                logger.info(str(post_cmd))
        else:
            logger.debug("No new changes in the repository.")

        if not pargs.interval:
            _log_exit("Single run completed.", 0, logger.info)
        else:
            logger.debug("Sleeping for {} seconds.".format(pargs.interval))
            time.sleep(pargs.interval)
    except KeyboardInterrupt:
        _log_exit("Exiting on keyboard interrupt.", 0, logger.info)
    except Exception as e:
        logger.error("Error: {}".format(e), exc_info=True)


def _convert_abspaths(args: Namespace):
    for pp in ['pre', 'post']:
        if getattr(args, '{}_action'.format(pp)):
            actpath = getattr(args, '{}_action'.format(pp))
            if not op.exists(actpath):
                logger.debug(
                    "{} action is not a file or does not exist.".format(pp)
                )
                continue
            if op.abspath(actpath) != actpath:
                logger.debug(
                    "Converting {}_action to absolute path.".format(pp)
                )
                setattr(args, '{}_action'.format(pp), op.abspath(actpath))


def main():
    args = parse_args()
    repo_path = args.repo_path

    if not os.path.exists(repo_path):
        logger.error("Repository path '{}' does not exist.".format(repo_path))
        return 1

    _convert_abspaths(args)

    logger.debug("Changing to repository path: {}".format(repo_path))
    os.chdir(repo_path)

    logger.debug('args: {}'.format(args.__dict__))

    if args.interval:
        print('Polling every {} seconds...'.format(args.interval))
    else:
        print('Running once...')
    while True:
        logger.debug("Main loop iteration | ARGS {}".format(args.__dict__))
        _mainloop(args)


if __name__ == "__main__":
    main()
