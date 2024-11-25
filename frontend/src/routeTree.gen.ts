/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file was automatically generated by TanStack Router.
// You should NOT make any changes in this file as it will be overwritten.
// Additionally, you should also exclude this file from your linter and/or formatter to prevent it from being checked or modified.

import { createFileRoute } from '@tanstack/react-router'

// Import Routes

import { Route as rootRoute } from './routes/__root'

// Create Virtual Routes

const R404LazyImport = createFileRoute('/404')()
const IndexLazyImport = createFileRoute('/')()
const GameGameIdLazyImport = createFileRoute('/game/$gameId')()

// Create/Update Routes

const R404LazyRoute = R404LazyImport.update({
  id: '/404',
  path: '/404',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/404.lazy').then((d) => d.Route))

const IndexLazyRoute = IndexLazyImport.update({
  id: '/',
  path: '/',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/index.lazy').then((d) => d.Route))

const GameGameIdLazyRoute = GameGameIdLazyImport.update({
  id: '/game/$gameId',
  path: '/game/$gameId',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/game.$gameId.lazy').then((d) => d.Route))

// Populate the FileRoutesByPath interface

declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/': {
      id: '/'
      path: '/'
      fullPath: '/'
      preLoaderRoute: typeof IndexLazyImport
      parentRoute: typeof rootRoute
    }
    '/404': {
      id: '/404'
      path: '/404'
      fullPath: '/404'
      preLoaderRoute: typeof R404LazyImport
      parentRoute: typeof rootRoute
    }
    '/game/$gameId': {
      id: '/game/$gameId'
      path: '/game/$gameId'
      fullPath: '/game/$gameId'
      preLoaderRoute: typeof GameGameIdLazyImport
      parentRoute: typeof rootRoute
    }
  }
}

// Create and export the route tree

export interface FileRoutesByFullPath {
  '/': typeof IndexLazyRoute
  '/404': typeof R404LazyRoute
  '/game/$gameId': typeof GameGameIdLazyRoute
}

export interface FileRoutesByTo {
  '/': typeof IndexLazyRoute
  '/404': typeof R404LazyRoute
  '/game/$gameId': typeof GameGameIdLazyRoute
}

export interface FileRoutesById {
  __root__: typeof rootRoute
  '/': typeof IndexLazyRoute
  '/404': typeof R404LazyRoute
  '/game/$gameId': typeof GameGameIdLazyRoute
}

export interface FileRouteTypes {
  fileRoutesByFullPath: FileRoutesByFullPath
  fullPaths: '/' | '/404' | '/game/$gameId'
  fileRoutesByTo: FileRoutesByTo
  to: '/' | '/404' | '/game/$gameId'
  id: '__root__' | '/' | '/404' | '/game/$gameId'
  fileRoutesById: FileRoutesById
}

export interface RootRouteChildren {
  IndexLazyRoute: typeof IndexLazyRoute
  R404LazyRoute: typeof R404LazyRoute
  GameGameIdLazyRoute: typeof GameGameIdLazyRoute
}

const rootRouteChildren: RootRouteChildren = {
  IndexLazyRoute: IndexLazyRoute,
  R404LazyRoute: R404LazyRoute,
  GameGameIdLazyRoute: GameGameIdLazyRoute,
}

export const routeTree = rootRoute
  ._addFileChildren(rootRouteChildren)
  ._addFileTypes<FileRouteTypes>()

/* ROUTE_MANIFEST_START
{
  "routes": {
    "__root__": {
      "filePath": "__root.tsx",
      "children": [
        "/",
        "/404",
        "/game/$gameId"
      ]
    },
    "/": {
      "filePath": "index.lazy.tsx"
    },
    "/404": {
      "filePath": "404.lazy.tsx"
    },
    "/game/$gameId": {
      "filePath": "game.$gameId.lazy.tsx"
    }
  }
}
ROUTE_MANIFEST_END */
