# Developer Test Packs

Feature test packs let a feature contribute development resources without editing
the framework or another feature's files.

The generator scans production item definitions under `Defs/ThingDefs_Items/`
for `EI_` items automatically. Add a test pack only when a feature needs custom
developer quantities, future non-item metadata, or explicit grouping.

Example:

```xml
<?xml version="1.0" encoding="utf-8"?>
<DeveloperTestPack>
  <defName>FS999_Example</defName>
  <label>Example future feature</label>
  <resources>
    <li defName="EI_ExampleRawItem" count="500" />
    <li defName="EI_ExampleFinishedItem" count="100" />
  </resources>
</DeveloperTestPack>
```

Files ending in `.disabled` are ignored. Test packs are source inputs only; they
are never copied into the public package or the staged developer package.
