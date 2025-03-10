<template>
  <div class="d-flex flex-row labeled-address-display align-center">
    <v-tooltip top open-delay="400" :disabled="!truncated">
      <template #activator="{ on }">
        <span
          data-cy="labeled-address-display"
          class="labeled-address-display__address"
          :class="xsOnly ? 'labeled-address-display__address--mobile' : null"
          v-on="on"
        >
          <v-chip label outlined class="labeled-address-display__chip">
            <v-avatar size="24" class="mr-2">
              <v-img :src="makeBlockie(address)" />
            </v-avatar>
            <span v-if="!!label" class="text-truncate">
              {{
                $t('labeled_address_display.label', {
                  label: label
                })
              }}
            </span>
            <span v-if="!!label && displayAddress && !smAndDown" class="px-1">
              {{ $t('labeled_address_display.divider') }}
            </span>
            <span
              v-if="!smAndDown || !label"
              :class="{ 'blur-content': !shouldShowAmount }"
            >
              {{ displayAddress }}
            </span>
          </v-chip>
        </span>
      </template>
      <span v-if="!!label"> {{ account.label }} <br /> </span>
      <span> {{ address }} </span>
    </v-tooltip>
    <div class="labeled-address-display__actions">
      <hash-link :text="account.address" buttons small :chain="account.chain" />
    </div>
  </div>
</template>

<script lang="ts">
import { GeneralAccount } from '@rotki/common/lib/account';
import {
  computed,
  defineComponent,
  PropType,
  toRefs
} from '@vue/composition-api';
import makeBlockie from 'ethereum-blockies-base64';
import { setupThemeCheck } from '@/composables/common';
import { setupDisplayData } from '@/composables/session';
import { truncateAddress, truncationPoints } from '@/filters';
import { randomHex } from '@/utils/data';

export default defineComponent({
  name: 'LabeledAddressDisplay',
  props: {
    account: { required: true, type: Object as PropType<GeneralAccount> }
  },
  setup(props) {
    const { account } = toRefs(props);
    const { currentBreakpoint } = setupThemeCheck();
    const { scrambleData, shouldShowAmount } = setupDisplayData();

    const xsOnly = computed(() => currentBreakpoint.value.xsOnly);
    const smAndDown = computed(() => currentBreakpoint.value.smAndDown);

    const address = computed<string>(() => {
      return scrambleData.value ? randomHex() : account.value.address;
    });

    const breakpoint = computed<string>(() => {
      return account.value.label.length > 0 && currentBreakpoint.value.mdAndDown
        ? 'sm'
        : currentBreakpoint.value.name;
    });

    const truncationLength = computed<number>(() => {
      let truncationPoint = truncationPoints[breakpoint.value];
      if (truncationPoint && account.value.label) {
        return 4;
      }
      return truncationPoint ?? 4;
    });

    const truncatedAddress = computed(() => {
      return truncateAddress(address.value, truncationLength.value);
    });

    const displayAddress = computed<string>(() => {
      if (truncatedAddress.value.length >= address.value.length) {
        return address.value;
      }
      return truncatedAddress.value;
    });

    const truncated = computed<boolean>(() => {
      if (truncatedAddress.value.length >= address.value.length) {
        return false;
      }
      return truncatedAddress.value.includes('...');
    });

    const label = computed<string>(() => {
      const bp = currentBreakpoint.value;
      const label = account.value.label;
      let length = -1;

      if (bp.xlOnly && label.length > 50) {
        length = 47;
      } else if (bp.lgOnly && label.length > 38) {
        length = 35;
      } else if (bp.md && label.length > 27) {
        length = 24;
      } else if (bp.smOnly && label.length > 19) {
        length = 16;
      }

      if (length > 0) {
        return label.substr(0, length) + '...';
      }

      return label;
    });

    return {
      xsOnly,
      smAndDown,
      truncated,
      label,
      displayAddress,
      shouldShowAmount,
      address,
      makeBlockie
    };
  }
});
</script>

<style scoped lang="scss">
.labeled-address-display {
  max-height: 30px;
  width: 100%;

  &__address {
    width: 100%;
    font-weight: 500;
    padding-top: 6px;
    padding-bottom: 6px;

    &--mobile {
      max-width: 120px;
    }

    ::v-deep {
      .v-chip {
        background-color: white !important;

        &--label {
          border-top-right-radius: 0 !important;
          border-bottom-right-radius: 0 !important;
        }
      }
    }
  }

  &__actions {
    height: 32px;
    background-color: var(--v-rotki-light-grey-base);
    border: 1px solid rgba(0, 0, 0, 0.12);
    border-left-width: 0;
    border-radius: 0 4px 4px 0;
    display: inline-block;
  }

  &__chip {
    width: 100%;
  }
}

.blur-content {
  filter: blur(0.75em);
}
</style>
