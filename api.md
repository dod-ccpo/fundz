# Fundz API

## Task Order

### Get task order

Get a task order.

Request:

```
GET /task-order/<number>
```

Response:

```json
{
  "id": 12,
  "number": "123-abc"
}
```

## PE Number

### Get PE number

Request:

```
GET  /pe-number/0103190JNO
```

Response:

```json
{
  "description": "Combatant HQ - NORAD",
  "number": "0103190JNO"
}
```

## Convenience / Utility Endpoints

### Root

Request:

```
GET /
```

Response:

```
{ "hello": "world" }
```
