# Data Engine: API reference (domain CRUD)

> **Generated** from the data engine's OpenAPI spec (`data-engine-openapi.json`, same folder).
> Don't edit by hand; regenerate it when the data engine changes. For conventions, errors and
> usage, read `DATA_ENGINE_GUIDE.md` first.

Every route needs `X-Data-API-Key`. The **Org** column says where the organization comes from.

## Endpoints

### Users

| Method | Path | Summary | Org | Body | Success | Errors | Query params |
|---|---|---|---|---|---|---|---|
| `POST` | `/users` | Create a user | none (global) | `UserCreate` | 201 `UserRead` | 409, 422 | — |
| `GET` | `/users` | Find a user by email | none (global) | — | 200 `Page_UserRead_` | 422 | `email`*, `limit`, `offset` |
| `GET` | `/users/{userId}` | Get a user | none (global) | — | 200 `UserRead` | 404, 422 | — |
| `PATCH` | `/users/{userId}` | Update a user | none (global) | `UserUpdate` | 200 `UserRead` | 404, 409, 422 | — |
| `GET` | `/users/{userId}/memberships` | List a user's memberships | none (global) | — | 200 `Page_MemberRead_` | 404, 422 | `limit`, `offset` |

### Organizations

| Method | Path | Summary | Org | Body | Success | Errors | Query params |
|---|---|---|---|---|---|---|---|
| `POST` | `/organizations` | Create an organization with its first member | none (global) | `OrganizationCreate` | 201 `OrganizationCreated` | 422 | — |
| `GET` | `/organizations/{orgId}` | Get an organization | path `orgId` | — | 200 `OrganizationRead` | 404, 422 | — |
| `PATCH` | `/organizations/{orgId}` | Update an organization | path `orgId` | `OrganizationUpdate` | 200 `OrganizationRead` | 404, 422 | — |
| `DELETE` | `/organizations/{orgId}` | Archive an organization | path `orgId` | — | 204 | 404, 422 | — |

### Members

| Method | Path | Summary | Org | Body | Success | Errors | Query params |
|---|---|---|---|---|---|---|---|
| `GET` | `/members/{memberId}` | Get a member | header | — | 200 `MemberRead` | 400, 404, 422 | — |
| `PATCH` | `/members/{memberId}` | Update a member | header | `MemberUpdate` | 200 `MemberRead` | 400, 404, 409, 422 | — |
| `GET` | `/members/{memberId}/projects` | List projects of a member's teams | header | — | 200 `Page_ProjectRead_` | 400, 404, 422 | `limit`, `offset` |
| `GET` | `/members/{memberId}/tasks` | List tasks assigned to a member | header | — | 200 `Page_TaskRead_` | 400, 404, 422 | `status`, `limit`, `offset` |
| `GET` | `/members/{memberId}/teams` | List a member's team memberships | header | — | 200 `Page_TeamMemberRead_` | 400, 404, 422 | `limit`, `offset` |
| `POST` | `/organizations/{orgId}/members` | Create a member | path `orgId` | `MemberCreate` | 201 `MemberRead` | 404, 409, 422 | — |
| `GET` | `/organizations/{orgId}/members` | List members of an organization | path `orgId` | — | 200 `Page_MemberRead_` | 404, 422 | `type`, `status`, `role`, `workspaceId`, `limit`, `offset` |

### Workspaces

| Method | Path | Summary | Org | Body | Success | Errors | Query params |
|---|---|---|---|---|---|---|---|
| `POST` | `/organizations/{orgId}/workspaces` | Create a workspace (department) | path `orgId` | `WorkspaceCreate` | 201 `WorkspaceRead` | 404, 409, 422 | — |
| `GET` | `/organizations/{orgId}/workspaces` | List workspaces of an organization | path `orgId` | — | 200 `Page_WorkspaceRead_` | 404, 422 | `archived`, `limit`, `offset` |
| `GET` | `/workspaces/{workspaceId}` | Get a workspace | header | — | 200 `WorkspaceRead` | 400, 404, 422 | — |
| `PATCH` | `/workspaces/{workspaceId}` | Update a workspace | header | `WorkspaceUpdate` | 200 `WorkspaceRead` | 400, 404, 409, 422 | — |
| `DELETE` | `/workspaces/{workspaceId}` | Archive a workspace | header | — | 204 | 400, 404, 422 | — |

### Teams

| Method | Path | Summary | Org | Body | Success | Errors | Query params |
|---|---|---|---|---|---|---|---|
| `GET` | `/teams/{teamId}` | Get a team | header | — | 200 `TeamRead` | 400, 404, 422 | — |
| `PATCH` | `/teams/{teamId}` | Update a team | header | `TeamUpdate` | 200 `TeamRead` | 400, 404, 409, 422 | — |
| `DELETE` | `/teams/{teamId}` | Archive a team | header | — | 204 | 400, 404, 422 | — |
| `POST` | `/teams/{teamId}/members` | Add a member to a team | header | `TeamMemberCreate` | 201 `TeamMemberRead` | 400, 404, 409, 422 | — |
| `GET` | `/teams/{teamId}/members` | List team members | header | — | 200 `Page_TeamMemberRead_` | 400, 404, 422 | `limit`, `offset` |
| `PATCH` | `/teams/{teamId}/members/{memberId}` | Update a team member's role | header | `TeamMemberUpdate` | 200 `TeamMemberRead` | 400, 404, 422 | — |
| `DELETE` | `/teams/{teamId}/members/{memberId}` | Remove a member from a team | header | — | 204 | 400, 404, 422 | — |
| `GET` | `/teams/{teamId}/projects` | List projects a team works on | header | — | 200 `Page_ProjectRead_` | 400, 404, 422 | `limit`, `offset` |
| `POST` | `/workspaces/{workspaceId}/teams` | Create a team | header | `TeamCreate` | 201 `TeamRead` | 400, 404, 409, 422 | — |
| `GET` | `/workspaces/{workspaceId}/teams` | List teams of a workspace | header | — | 200 `Page_TeamRead_` | 400, 404, 422 | `archived`, `limit`, `offset` |

### Projects

| Method | Path | Summary | Org | Body | Success | Errors | Query params |
|---|---|---|---|---|---|---|---|
| `GET` | `/projects/{projectId}` | Get a project | header | — | 200 `ProjectRead` | 400, 404, 422 | — |
| `PATCH` | `/projects/{projectId}` | Update a project | header | `ProjectUpdate` | 200 `ProjectRead` | 400, 404, 409, 422 | — |
| `DELETE` | `/projects/{projectId}` | Archive a project | header | — | 204 | 400, 404, 422 | — |
| `POST` | `/projects/{projectId}/teams` | Add a team to a project | header | `ProjectTeamCreate` | 201 `ProjectTeamRead` | 400, 404, 409, 422 | — |
| `GET` | `/projects/{projectId}/teams` | List teams on a project | header | — | 200 `Page_ProjectTeamRead_` | 400, 404, 422 | `limit`, `offset` |
| `DELETE` | `/projects/{projectId}/teams/{teamId}` | Remove a team from a project | header | — | 204 | 400, 404, 409, 422 | — |
| `POST` | `/workspaces/{workspaceId}/projects` | Create a project | header | `ProjectCreate` | 201 `ProjectRead` | 400, 404, 409, 422 | — |
| `GET` | `/workspaces/{workspaceId}/projects` | List projects of a workspace | header | — | 200 `Page_ProjectRead_` | 400, 404, 422 | `archived`, `status`, `limit`, `offset` |

### Work-items

| Method | Path | Summary | Org | Body | Success | Errors | Query params |
|---|---|---|---|---|---|---|---|
| `POST` | `/projects/{projectId}/work-items` | Create a work item | header | `WorkItemCreate` | 201 `WorkItemRead` | 400, 404, 422 | — |
| `GET` | `/projects/{projectId}/work-items` | List work items of a project | header | — | 200 `Page_WorkItemRead_` | 400, 404, 422 | `status`, `type`, `priority`, `limit`, `offset` |
| `GET` | `/work-items/{workItemId}` | Get a work item | header | — | 200 `WorkItemRead` | 400, 404, 422 | — |
| `PATCH` | `/work-items/{workItemId}` | Update a work item | header | `WorkItemUpdate` | 200 `WorkItemRead` | 400, 404, 422 | — |
| `DELETE` | `/work-items/{workItemId}` | Delete a work item | header | — | 204 | 400, 404, 422 | — |

### Sprints

| Method | Path | Summary | Org | Body | Success | Errors | Query params |
|---|---|---|---|---|---|---|---|
| `GET` | `/projects/{projectId}/sprints` | List sprints of a project | header | — | 200 `Page_SprintRead_` | 400, 404, 422 | `teamId`, `status`, `limit`, `offset` |
| `POST` | `/projects/{projectId}/teams/{teamId}/sprints` | Create a sprint for a team in a project | header | `SprintCreate` | 201 `SprintRead` | 400, 404, 409, 422 | — |
| `GET` | `/sprints/{sprintId}` | Get a sprint | header | — | 200 `SprintRead` | 400, 404, 422 | — |
| `PATCH` | `/sprints/{sprintId}` | Update a sprint | header | `SprintUpdate` | 200 `SprintRead` | 400, 404, 409, 422 | — |
| `DELETE` | `/sprints/{sprintId}` | Delete a sprint | header | — | 204 | 400, 404, 422 | — |

### Tasks

| Method | Path | Summary | Org | Body | Success | Errors | Query params |
|---|---|---|---|---|---|---|---|
| `POST` | `/projects/{projectId}/tasks` | Create a task | header | `TaskCreate` | 201 `TaskRead` | 400, 404, 422 | — |
| `GET` | `/projects/{projectId}/tasks` | List tasks of a project | header | — | 200 `Page_TaskRead_` | 400, 404, 422 | `status`, `priority`, `assigneeId`, `sprintId`, `workItemId`, `backlog`, `limit`, `offset` |
| `GET` | `/tasks/by-key/{key}` | Get a task by its key | header | — | 200 `TaskRead` | 400, 404, 422 | — |
| `GET` | `/tasks/{taskId}` | Get a task | header | — | 200 `TaskRead` | 400, 404, 422 | — |
| `PATCH` | `/tasks/{taskId}` | Update a task | header | `TaskUpdate` | 200 `TaskRead` | 400, 404, 422 | — |
| `DELETE` | `/tasks/{taskId}` | Delete a task | header | — | 204 | 400, 404, 422 | — |

`*` = required query parameter. Every list route also takes `limit` (1–200, default 50) and `offset` (≥ 0, default 0).

## Schemas

### Enums

| Enum | Values |
|---|---|
| `MemberRole` | `OWNER`, `MEMBER` |
| `MemberStatus` | `ACTIVE`, `INACTIVE` |
| `MemberType` | `HUMAN`, `AI` |
| `Priority` | `LOW`, `MEDIUM`, `HIGH`, `URGENT` |
| `ProjectStatus` | `ACTIVE`, `COMPLETED` |
| `SprintStatus` | `PLANNED`, `ACTIVE`, `COMPLETED`, `CANCELLED` |
| `TaskStatus` | `TODO`, `IN_PROGRESS`, `REVIEW`, `DONE`, `BLOCKED` |
| `TeamMemberRole` | `LEAD`, `MEMBER` |
| `WorkItemStatus` | `OPEN`, `IN_PROGRESS`, `DONE`, `CANCELLED` |
| `WorkItemType` | `FEATURE`, `STORY`, `BUG` |

### `CreatorMember`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `role` | MemberRole | no | `"OWNER"` | — |

### `ErrorResponse`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `code` | string | yes | — | — |
| `message` | string | yes | — | — |
| `field` | string \| null | no | — | — |

### `MemberCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `type` | MemberType | yes | — | — |
| `userId` | string(uuid) \| null | no | — | — |
| `name` | string \| null | no | — | min 1, max 100 |
| `email` | string(email) \| null | no | — | — |
| `role` | MemberRole | no | `"MEMBER"` | — |
| `status` | MemberStatus | no | `"ACTIVE"` | — |
| `workspaceId` | string(uuid) \| null | no | — | — |
| `createdById` | string(uuid) \| null | no | — | — |

### `MemberRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `id` | string(uuid) | yes | — | — |
| `createdAt` | string(date-time) | yes | — | — |
| `updatedAt` | string(date-time) | yes | — | — |
| `organizationId` | string(uuid) | yes | — | — |
| `userId` | string(uuid) \| null | yes | — | — |
| `workspaceId` | string(uuid) \| null | yes | — | — |
| `createdById` | string(uuid) \| null | yes | — | — |
| `type` | MemberType | yes | — | — |
| `name` | string \| null | yes | — | — |
| `email` | string \| null | yes | — | — |
| `role` | MemberRole | yes | — | — |
| `status` | MemberStatus | yes | — | — |

### `MemberUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `role` | MemberRole | no | — | — |
| `status` | MemberStatus | no | — | — |
| `workspaceId` | string(uuid) \| null | no | — | — |
| `name` | string \| null | no | — | min 1, max 100 |
| `email` | string(email) \| null | no | — | — |

### `OrganizationCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | yes | — | min 1, max 100 |
| `description` | string \| null | no | — | max 5000 |
| `createdById` | string(uuid) | yes | — | — |
| `creatorMember` | CreatorMember | no | — | — |

### `OrganizationCreated`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `organization` | OrganizationRead | yes | — | — |
| `member` | MemberRead | yes | — | — |

### `OrganizationRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `id` | string(uuid) | yes | — | — |
| `createdAt` | string(date-time) | yes | — | — |
| `updatedAt` | string(date-time) | yes | — | — |
| `createdById` | string(uuid) | yes | — | — |
| `name` | string | yes | — | — |
| `description` | string \| null | yes | — | — |
| `archivedAt` | string(date-time) \| null | yes | — | — |

### `OrganizationUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | no | — | min 1, max 100 |
| `description` | string \| null | no | — | max 5000 |
| `archived` | boolean | no | — | — |

### `Page_MemberRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<MemberRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `Page_ProjectRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<ProjectRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `Page_ProjectTeamRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<ProjectTeamRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `Page_SprintRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<SprintRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `Page_TaskRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<TaskRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `Page_TeamMemberRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<TeamMemberRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `Page_TeamRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<TeamRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `Page_UserRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<UserRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `Page_WorkItemRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<WorkItemRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `Page_WorkspaceRead_`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `items` | array<WorkspaceRead> | yes | — | — |
| `limit` | integer | yes | — | — |
| `offset` | integer | yes | — | — |
| `hasMore` | boolean | yes | — | — |

### `ProjectCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `key` | string | yes | — | pattern `^[A-Z]{2,10}$` |
| `name` | string | yes | — | min 1, max 100 |
| `description` | string \| null | no | — | max 5000 |
| `status` | ProjectStatus | no | `"ACTIVE"` | — |
| `createdById` | string(uuid) | yes | — | — |

### `ProjectRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `id` | string(uuid) | yes | — | — |
| `createdAt` | string(date-time) | yes | — | — |
| `updatedAt` | string(date-time) | yes | — | — |
| `organizationId` | string(uuid) | yes | — | — |
| `workspaceId` | string(uuid) | yes | — | — |
| `createdById` | string(uuid) | yes | — | — |
| `key` | string | yes | — | — |
| `name` | string | yes | — | — |
| `description` | string \| null | yes | — | — |
| `status` | ProjectStatus | yes | — | — |
| `archivedAt` | string(date-time) \| null | yes | — | — |

### `ProjectTeamCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `teamId` | string(uuid) | yes | — | — |

### `ProjectTeamRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `projectId` | string(uuid) | yes | — | — |
| `teamId` | string(uuid) | yes | — | — |
| `organizationId` | string(uuid) | yes | — | — |
| `joinedAt` | string(date-time) | yes | — | — |

### `ProjectUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | no | — | min 1, max 100 |
| `description` | string \| null | no | — | max 5000 |
| `status` | ProjectStatus | no | — | — |
| `archived` | boolean | no | — | — |

### `SprintCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | yes | — | min 1, max 100 |
| `goal` | string \| null | no | — | max 5000 |
| `status` | SprintStatus | no | `"PLANNED"` | — |
| `startDate` | string(date) \| null | no | — | — |
| `endDate` | string(date) \| null | no | — | — |
| `createdById` | string(uuid) | yes | — | — |

### `SprintRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `id` | string(uuid) | yes | — | — |
| `createdAt` | string(date-time) | yes | — | — |
| `updatedAt` | string(date-time) | yes | — | — |
| `organizationId` | string(uuid) | yes | — | — |
| `projectId` | string(uuid) | yes | — | — |
| `teamId` | string(uuid) | yes | — | — |
| `createdById` | string(uuid) | yes | — | — |
| `name` | string | yes | — | — |
| `goal` | string \| null | yes | — | — |
| `status` | SprintStatus | yes | — | — |
| `startDate` | string(date) \| null | yes | — | — |
| `endDate` | string(date) \| null | yes | — | — |

### `SprintUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | no | — | min 1, max 100 |
| `goal` | string \| null | no | — | max 5000 |
| `status` | SprintStatus | no | — | — |
| `startDate` | string(date) \| null | no | — | — |
| `endDate` | string(date) \| null | no | — | — |

### `TaskCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `title` | string | yes | — | min 1, max 200 |
| `description` | string \| null | no | — | max 5000 |
| `requirements` | string \| null | no | — | max 10000 |
| `acceptanceCriteria` | string \| null | no | — | max 10000 |
| `priority` | Priority | no | `"MEDIUM"` | — |
| `status` | TaskStatus | no | `"TODO"` | — |
| `dueDate` | string(date-time) \| null | no | — | — |
| `completedAt` | string(date-time) \| null | no | — | — |
| `workItemId` | string(uuid) \| null | no | — | — |
| `sprintId` | string(uuid) \| null | no | — | — |
| `assigneeId` | string(uuid) \| null | no | — | — |
| `createdById` | string(uuid) | yes | — | — |

### `TaskRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `id` | string(uuid) | yes | — | — |
| `createdAt` | string(date-time) | yes | — | — |
| `updatedAt` | string(date-time) | yes | — | — |
| `organizationId` | string(uuid) | yes | — | — |
| `projectId` | string(uuid) | yes | — | — |
| `number` | integer | yes | — | — |
| `key` | string | yes | — | — |
| `workItemId` | string(uuid) \| null | yes | — | — |
| `sprintId` | string(uuid) \| null | yes | — | — |
| `assigneeId` | string(uuid) \| null | yes | — | — |
| `createdById` | string(uuid) | yes | — | — |
| `title` | string | yes | — | — |
| `description` | string \| null | yes | — | — |
| `requirements` | string \| null | yes | — | — |
| `acceptanceCriteria` | string \| null | yes | — | — |
| `priority` | Priority | yes | — | — |
| `status` | TaskStatus | yes | — | — |
| `dueDate` | string(date-time) \| null | yes | — | — |
| `completedAt` | string(date-time) \| null | yes | — | — |

### `TaskUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `title` | string | no | — | min 1, max 200 |
| `description` | string \| null | no | — | max 5000 |
| `requirements` | string \| null | no | — | max 10000 |
| `acceptanceCriteria` | string \| null | no | — | max 10000 |
| `priority` | Priority | no | — | — |
| `status` | TaskStatus | no | — | — |
| `dueDate` | string(date-time) \| null | no | — | — |
| `completedAt` | string(date-time) \| null | no | — | — |
| `workItemId` | string(uuid) \| null | no | — | — |
| `sprintId` | string(uuid) \| null | no | — | — |
| `assigneeId` | string(uuid) \| null | no | — | — |

### `TeamCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | yes | — | min 1, max 100 |
| `description` | string \| null | no | — | max 5000 |
| `createdById` | string(uuid) | yes | — | — |

### `TeamMemberCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `memberId` | string(uuid) | yes | — | — |
| `role` | TeamMemberRole | no | `"MEMBER"` | — |

### `TeamMemberRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `teamId` | string(uuid) | yes | — | — |
| `memberId` | string(uuid) | yes | — | — |
| `organizationId` | string(uuid) | yes | — | — |
| `role` | TeamMemberRole | yes | — | — |
| `joinedAt` | string(date-time) | yes | — | — |

### `TeamMemberUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `role` | TeamMemberRole | no | — | — |

### `TeamRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `id` | string(uuid) | yes | — | — |
| `createdAt` | string(date-time) | yes | — | — |
| `updatedAt` | string(date-time) | yes | — | — |
| `organizationId` | string(uuid) | yes | — | — |
| `workspaceId` | string(uuid) | yes | — | — |
| `createdById` | string(uuid) | yes | — | — |
| `name` | string | yes | — | — |
| `description` | string \| null | yes | — | — |
| `archivedAt` | string(date-time) \| null | yes | — | — |

### `TeamUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | no | — | min 1, max 100 |
| `description` | string \| null | no | — | max 5000 |
| `archived` | boolean | no | — | — |

### `UserCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | yes | — | min 1, max 100 |
| `email` | string(email) | yes | — | — |

### `UserRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `id` | string(uuid) | yes | — | — |
| `createdAt` | string(date-time) | yes | — | — |
| `updatedAt` | string(date-time) | yes | — | — |
| `name` | string | yes | — | — |
| `email` | string | yes | — | — |

### `UserUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | no | — | min 1, max 100 |
| `email` | string(email) | no | — | — |

### `WorkItemCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `title` | string | yes | — | min 1, max 200 |
| `description` | string \| null | no | — | max 5000 |
| `type` | WorkItemType | yes | — | — |
| `priority` | Priority | no | `"MEDIUM"` | — |
| `status` | WorkItemStatus | no | `"OPEN"` | — |
| `createdById` | string(uuid) | yes | — | — |

### `WorkItemRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `id` | string(uuid) | yes | — | — |
| `createdAt` | string(date-time) | yes | — | — |
| `updatedAt` | string(date-time) | yes | — | — |
| `organizationId` | string(uuid) | yes | — | — |
| `projectId` | string(uuid) | yes | — | — |
| `createdById` | string(uuid) | yes | — | — |
| `title` | string | yes | — | — |
| `description` | string \| null | yes | — | — |
| `type` | WorkItemType | yes | — | — |
| `priority` | Priority | yes | — | — |
| `status` | WorkItemStatus | yes | — | — |

### `WorkItemUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `title` | string | no | — | min 1, max 200 |
| `description` | string \| null | no | — | max 5000 |
| `type` | WorkItemType | no | — | — |
| `priority` | Priority | no | — | — |
| `status` | WorkItemStatus | no | — | — |

### `WorkspaceCreate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | yes | — | min 1, max 100 |
| `description` | string \| null | no | — | max 5000 |
| `createdById` | string(uuid) | yes | — | — |

### `WorkspaceRead`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `id` | string(uuid) | yes | — | — |
| `createdAt` | string(date-time) | yes | — | — |
| `updatedAt` | string(date-time) | yes | — | — |
| `organizationId` | string(uuid) | yes | — | — |
| `createdById` | string(uuid) | yes | — | — |
| `name` | string | yes | — | — |
| `description` | string \| null | yes | — | — |
| `archivedAt` | string(date-time) \| null | yes | — | — |

### `WorkspaceUpdate`

| Field | Type | Required | Default | Constraints |
|---|---|---|---|---|
| `name` | string | no | — | min 1, max 100 |
| `description` | string \| null | no | — | max 5000 |
| `archived` | boolean | no | — | — |
