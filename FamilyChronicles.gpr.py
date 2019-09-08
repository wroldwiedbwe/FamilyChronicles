register(REPORT,
    id   = 'FamilyChronicles',
    name = _('Family Chronicles'),
    description = _("Produces a summary of a family sheet showing limited information "
                    "about a person and his/her partners and children."),
    version = '0.0.1',
    gramps_target_version = "5.1",
    status = STABLE,
    fname = 'FamilyChronicles.py',
    authors = ["Thomas Bütikofer"],
    authors_email = ["t.buetikofer.mail@gmail.com"],
    category = CATEGORY_TEXT,
    reportclass = 'FamilyChronicles',
    optionclass = 'FamilyChroniclesOptions',
    report_modes = [REPORT_MODE_CLI, REPORT_MODE_GUI, REPORT_MODE_BKI],
    require_active = True
    )