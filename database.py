new_database = {
    'listCompanies': [{
        'id': 'new-company-1',
        '__typename': 'Company',
        'name': 'Company A',
        'industry': 'Tech'
    }],
    'listDepartments': [{
        'id': 'new-department-1',
        '__typename': 'Department',
        'name': 'Engineering',
        'companyID': 'new-company-1'
    }, {
        'id': 'new-department-2',
        '__typename': 'Department',
        'name': 'Marketing',
        'companyID': 'new-company-1'
    }],
    'listTeams': [{
        'id': 'new-team-1',
        '__typename': 'Team',
        'name': 'Backend Team',
        'departmentID': 'new-department-1'
    }, {
        'id': 'new-team-2',
        '__typename': 'Team',
        'name': 'Frontend Team',
        'departmentID': 'new-department-1'
    }, {
        'id': 'new-team-3',
        '__typename': 'Team',
        'name': 'Digital Marketing',
        'departmentID': 'new-department-2'
    }],
    'listEmployees': [{
        'id': 'new-employee-1',
        '__typename': 'Employee',
        'name': 'John Doe',
        'position': 'Software Engineer',
        'teamID': 'new-team-1'
    }, {
        'id': 'new-employee-2',
        '__typename': 'Employee',
        'name': 'Jane Smith',
        'position': 'Frontend Developer',
        'teamID': 'new-team-2'
    }, {
        'id': 'new-employee-3',
        '__typename': 'Employee',
        'name': 'Alex Brown',
        'position': 'Marketing Specialist',
        'teamID': 'new-team-3'
    }],
    'listTasks': [{
        'id': 'new-task-1',
        '__typename': 'Task',
        'description': 'Implement new feature',
        'employeeID': 'new-employee-1'
    }, {
        'id': 'new-task-2',
        '__typename': 'Task',
        'description': 'Design homepage layout',
        'employeeID': 'new-employee-2'
    }, {
        'id': 'new-task-3',
        '__typename': 'Task',
        'description': 'Create social media campaign',
        'employeeID': 'new-employee-3'
    }]
}
