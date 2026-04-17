/**
 * TEMPLATE: Content registry for rich HTML content components
 *
 * CUSTOMIZE: Replace the collection name and add entries for each
 * content item that has a rich content component.
 *
 * Items not in this registry render only their summary/longDescription.
 * Items listed here render the full structured content below the summary.
 */

import type { ComponentType } from 'react'

type ContentModule = { default: ComponentType }

const contentRegistry: Record<string, () => Promise<ContentModule>> = {
  // CUSTOMIZE: Add one entry per published document
  // 'document-slug': () => import('./document-slug'),
}

export function hasRichContent(slug: string): boolean {
  return slug in contentRegistry
}

export async function getRichContent(slug: string): Promise<ComponentType | null> {
  const loader = contentRegistry[slug]
  if (!loader) return null
  const mod = await loader()
  return mod.default
}
